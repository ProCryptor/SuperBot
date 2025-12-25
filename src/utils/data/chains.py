from src.models.chain import Chain

chain_mapping = {
    'BASE': Chain(
        chain_name='BASE',
        native_token='ETH',
        rpc='https://mainnet.base.org',
        chain_id=8453
    ),
    'ARBITRUM': Chain(
        chain_name='ARBITRUM',
        native_token='ETH',
        rpc='https://arb1.arbitrum.io/rpc',
        chain_id=42161
    ),
    'OPTIMISM': Chain(
        chain_name='OPTIMISM',
        native_token='ETH',
        rpc='https://mainnet.optimism.io',
        chain_id=10
    ),
    'ETHEREUM': Chain(
        chain_name='ETHEREUM',
        native_token='ETH',
        rpc='https://rpc.ankr.com/eth',
        chain_id=1
    ),
    'LINEA': Chain(
        chain_name='LINEA',
        native_token='ETH',
        rpc='https://rpc.linea.build',
        chain_id=59144
    ),
}
