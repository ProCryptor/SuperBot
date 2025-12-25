# src/utils/data/chain_modules.py
# Минимальная версия для запуска бота без краша.
# Позже можно расширить реальными модулями.

from src.modules.swaps.uniswap.uniswap import Uniswap  # Если uniswap.py существует
# Если uniswap.py ещё нет — пока закомментируй выше и используй заглушку

# Заглушка для всех свапов (чтобы бот не падал)
async def process_uniswap(route, chain):
    print(f"[STUB] Uniswap swap on {chain.chain_name} for wallet {route.wallet.private_key[:8]}...")
    return True

async def process_matcha_swap(route, chain):
    print(f"[STUB] Matcha swap on {chain.chain_name}...")
    return True

async def process_bungee_swap(route, chain):
    print(f"[STUB] Bungee bridge/swap on {chain.chain_name}...")
    return True

async def process_owlto_swap(route, chain):
    print(f"[STUB] Owlto swap on {chain.chain_name}...")
    return True

async def process_relay_swap(route, chain):
    print(f"[STUB] Relay swap on {chain.chain_name}...")
    return True

async def process_rubyscore_vote(route, chain):
    print(f"[STUB] RubyScore vote on {chain.chain_name}...")
    return True

async def process_wrapper_unwrapper(route, chain):
    print(f"[STUB] Wrap/Unwrap ETH on {chain.chain_name}...")
    return True

async def process_deploy(route, chain):
    print(f"[STUB] Contract deploy on {chain.chain_name}...")
    return True

async def process_random_swaps(route, chain):
    print(f"[STUB] Random swaps on {chain.chain_name}...")
    return True

async def process_swap_all_to_eth(route, chain):
    print(f"[STUB] Swap all to ETH on {chain.chain_name}...")
    return True

async def process_base_activities(route, chain):
    print(f"[STUB] Base random activities on {chain.chain_name}...")
    return True

# Список доступных модулей для каждой цепочки
CHAIN_MODULES = {
    'BASE': ['UNISWAP', 'MATCHA_SWAP', 'BUNGEE_SWAP', 'OWLTO_SWAP', 'RELAY_SWAP'],
    'OPTIMISM': ['UNISWAP'],
    'ARBITRUM': ['UNISWAP'],
    'LINEA': ['UNISWAP'],
    'ETHEREUM': ['UNISWAP'],
}

# Связь имени модуля → функция-обработчик
MODULE_HANDLERS = {
    'UNISWAP': process_uniswap,
    'MATCHA_SWAP': process_matcha_swap,
    'BUNGEE_SWAP': process_bungee_swap,
    'OWLTO_SWAP': process_owlto_swap,
    'RELAY_SWAP': process_relay_swap,
    'RUBYSCORE_VOTE': process_rubyscore_vote,
    'WRAPPER_UNWRAPPER': process_wrapper_unwrapper,
    'CONTRACT_DEPLOY': process_deploy,
    'RANDOM_SWAPS': process_random_swaps,
    'SWAP_ALL_TO_ETH': process_swap_all_to_eth,
    'RANDOM_TXS': process_base_activities,
}
