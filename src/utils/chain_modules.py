# src/utils/chain_modules.py
import random
from src.modules.swaps.uniswap.uniswap import Uniswap
from src.modules.swaps.matcha.matcha_transaction import create_matcha_swap_tx
from src.modules.swaps.bungee.bungee_transaction import create_bungee_swap_tx
from src.modules.swaps.relayswap.relay_transaction import create_relay_swap_tx
from loguru import logger

async def process_uniswap(route, chain):
    try:
        uniswap = Uniswap(
            private_key=route.wallet.private_key,
            proxy=route.wallet.proxy,
            from_token='ETH',
            to_token='USDC',
            amount=random.uniform(0.001, 0.005),
            use_percentage=False,
            swap_percentage=0.0,
            swap_all_balance=False,
            chain=chain
        )
        success = await uniswap.swap()
        if success:
            logger.success(f"Uniswap swap successful on {chain.chain_name}")
            return True
        else:
            logger.error(f"Uniswap swap failed on {chain.chain_name}")
            return False
    except Exception as e:
        logger.error(f"Uniswap error: {e}")
        return False

async def process_matcha_swap(route, chain):
    try:
        # Используем фабрику MatchaSwap
        matcha = MatchaSwap(
            private_key=route.wallet.private_key,
            from_token='ETH',
            to_token='USDC',
            amount=random.uniform(0.001, 0.005),
            use_percentage=False,
            swap_percentage=0.0,
            swap_all_balance=False,
            proxy=route.wallet.proxy,
            chain=chain
        )
        success = await matcha.swap()
        if success:
            logger.success(f"Matcha swap successful on {chain.chain_name}")
            return True
        else:
            logger.error(f"Matcha swap failed on {chain.chain_name}")
            return False
    except Exception as e:
        logger.error(f"Matcha error: {e}")
        return False

async def process_bungee_swap(route, chain):
    try:
        bungee = BungeeSwap(
            private_key=route.wallet.private_key,
            from_token='ETH',
            to_token='USDC',
            amount=random.uniform(0.001, 0.005),
            use_percentage=False,
            swap_percentage=0.0,
            swap_all_balance=False,
            proxy=route.wallet.proxy,
            chain=chain
        )
        success = await bungee.swap()
        if success:
            logger.success(f"Bungee swap successful on {chain.chain_name}")
            return True
        else:
            logger.error(f"Bungee swap failed on {chain.chain_name}")
            return False
    except Exception as e:
        logger.error(f"Bungee error: {e}")
        return False

async def process_relay_swap(route, chain):
    try:
        relay = RelaySwap(
            private_key=route.wallet.private_key,
            from_token='ETH',
            to_token='USDC',
            amount=random.uniform(0.001, 0.005),
            use_percentage=False,
            swap_percentage=0.0,
            swap_all_balance=False,
            proxy=route.wallet.proxy,
            chain=chain
        )
        success = await relay.swap()
        if success:
            logger.success(f"Relay swap successful on {chain.chain_name}")
            return True
        else:
            logger.error(f"Relay swap failed on {chain.chain_name}")
            return False
    except Exception as e:
        logger.error(f"Relay swap error: {e}")
        return False

# Список модулей для цепочек (добавь свапы)
CHAIN_MODULES = {
    'BASE': ['UNISWAP', 'MATCHA_SWAP', 'BUNGEE_SWAP', 'RELAY_SWAP'],
    'OPTIMISM': ['UNISWAP', 'MATCHA_SWAP'],
    'ARBITRUM': ['UNISWAP', 'MATCHA_SWAP'],
    'LINEA': ['UNISWAP'],
    'ETHEREUM': ['UNISWAP'],
}

# Связь задачи → функция
MODULE_HANDLERS = {
    'UNISWAP': process_uniswap,
    'MATCHA_SWAP': process_matcha_swap,
    'BUNGEE_SWAP': process_bungee_swap,
    'RELAY_SWAP': process_relay_swap,
    # ... твои другие задачи (bridge, vote и т.д.)
}
