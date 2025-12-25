from .interfaces import DEX, RequestClient, Refuel, Messenger, Landing, Minter, Blockchain, Creator, Logger
from config import UniswapSettings
from src.modules.swaps.uniswap.uniswap import Uniswap


async def process_uniswap(route, chain) -> bool:
    """
    Handler для UNISWAP.
    Вызывается из main.py через MODULE_HANDLERS
    """
    wallet = route.wallet

    swapper = Uniswap(
        private_key=wallet.private_key,
        proxy=wallet.proxy,
        from_token=UniswapSettings.from_token,
        to_token=UniswapSettings.to_token,
        amount=UniswapSettings.amount,
        use_percentage=UniswapSettings.use_percentage,
        swap_percentage=UniswapSettings.swap_percentage,
        swap_all_balance=UniswapSettings.swap_all_balance,
        chain=chain,
    )

    result = await swapper.swap()
    return bool(result)
