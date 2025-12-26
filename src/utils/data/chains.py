from src.models.chain import Chain

BASE = Chain(
    chain_name='BASE',
    chain_id=8453,
    rpc='https://mainnet.base.org',
    scan='https://basescan.org/tx',
    native_token='ETH'
)

OPTIMISM = Chain(
    chain_name='OPTIMISM',
    chain_id=10,
    rpc='https://mainnet.optimism.io',
    scan='https://optimistic.etherscan.io/tx',
    native_token='ETH'
)

ARBITRUM = Chain(
    chain_name='ARBITRUM',
    chain_id=42161,
    rpc='https://arb1.arbitrum.io/rpc',
    scan='https://arbiscan.io/tx',
    native_token='ETH'
)

ETHEREUM = Chain(
    chain_name='ETHEREUM',
    chain_id=1,
    rpc='https://eth.llamarpc.com',
    scan='https://etherscan.io/tx',
    native_token='ETH'
)

LINEA = Chain(
    chain_name='LINEA',
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
