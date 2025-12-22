class Chain:
    def __init__(self, chain_id: int, rpc: str, scan: str, native_token: str) -> None:
        self.chain_id = chain_id
        self.rpc = rpc
        self.scan = scan
        self.native_token = native_token

BASE = Chain(
    chain_id=8453,
    rpc='https://mainnet.base.org',
    scan='https://basescan.org/tx',
    native_token='ETH'
)

OPTIMISM = Chain(
    chain_id=10,
    rpc='https://mainnet.optimism.io',
    scan='https://optimistic.etherscan.io/tx',
    native_token='ETH'
)

ARBITRUM = Chain(
    chain_id=42161,
    rpc='https://arb1.arbitrum.io/rpc',
    scan='https://arbiscan.io/tx',
    native_token='ETH'
)

ETHEREUM = Chain(
    chain_id=1,
    rpc='https://rpc.ankr.com/eth',
    scan='https://etherscan.io/tx',
    native_token='ETH'
)

LINEA = Chain(
    chain_id=59144,
    rpc='https://rpc.linea.build',
    scan='https://lineascan.build/tx',
    native_token='ETH'
)

chain_mapping = {
    'BASE': BASE,
    'OPTIMISM': OPTIMISM,
    'ARBITRUM': ARBITRUM,
    'ETHEREUM': ETHEREUM,
    'LINEA': LINEA,
}

