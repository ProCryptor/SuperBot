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

chain_mapping = {
    'BASE': BASE,
}
