from typing import Optional, Union, Callable, Awaitable
from asyncio import sleep

from web3.contract import AsyncContract
from web3 import AsyncWeb3
from loguru import logger

from src.models.contracts import ERC20
from eth_typing import Address, HexStr, ChecksumAddress


class Utils:
    @staticmethod
    def load_contract(
        address: str,
        web3: AsyncWeb3,
        abi: list
    ) -> Optional[AsyncContract]:
        if not address:
            return None
        return web3.eth.contract(
            address=web3.to_checksum_address(address),
            abi=abi
        )

    async def get_decimals(self, token_address: str, web3: AsyncWeb3) -> int:
        contract = self.load_contract(token_address, web3, ERC20.abi)
        return await contract.functions.decimals().call()

    @staticmethod
    async def check_allowance(
        web3: AsyncWeb3,
        token_address: str,
        owner: Address,
        spender: str
    ) -> int:
        try:
            contract = web3.eth.contract(
                address=web3.to_checksum_address(token_address),
                abi=ERC20.abi
            )
            allowance = await contract.functions.allowance(
                owner,
                web3.to_checksum_address(spender)
            ).call()
            return int(allowance)
        except Exception as e:
            logger.error(f"check_allowance failed: {e}")
            return 0

    async def approve_token(
        self,
        *,
        amount: int,
        private_key: str,
        token_address: str,
        spender: str,
        wallet_address: Address,
        web3: AsyncWeb3
    ) -> Optional[HexStr]:
        allowance = await self.check_allowance(
            web3, token_address, wallet_address, spender
        )

        if allowance >= amount:
            return None  # апрув не нужен

        logger.info("🛠️ Approving token...")

        contract = self.load_contract(token_address, web3, ERC20.abi)

        tx = await contract.functions.approve(
            web3.to_checksum_address(spender),
            2**256 - 1
        ).build_transaction({
            "from": wallet_address,
            "nonce": await web3.eth.get_transaction_count(wallet_address),
            "gasPrice": await web3.eth.gas_price,
            "chainId": await web3.eth.chain_id,
        })

        signed = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = await web3.eth.send_raw_transaction(signed.raw_transaction)

        await web3.eth.wait_for_transaction_receipt(tx_hash)
        logger.success("✔️ Token approved")

        return web3.to_hex(tx_hash)

    async def setup_decimals(
        self,
        is_native: bool,
        token_address: str,
        web3: AsyncWeb3
    ) -> int:
        return 18 if is_native else await self.get_decimals(token_address, web3)

    async def create_amount(
            self, is_native: bool, from_token_address: str, web3: AsyncWeb3, amount: float
    ) -> int:
        decimals = await self.setup_decimals(is_native, from_token_address, web3)
        amount = int(amount * 10 ** decimals)
        return amount
