import random
import asyncio
from loguru import logger

from src.models.chain import Chain
from src.utils.chain_modules import CHAIN_MODULES, MODULE_HANDLERS
from src.utils.data.chains import chain_mapping


class SwapExecutor:
    def __init__(self, route, planner, memory):
        self.route = route
        self.planner = planner
        self.memory = memory

    async def run_swap_day(self, min_swaps=2, max_swaps=4):
        swaps_count = random.randint(min_swaps, max_swaps)
        logger.info(f"SWAP DAY: planning {swaps_count} swaps")

        for i in range(swaps_count):
            chain_name = self.planner.choose_swap_chain()
            if not chain_name:
                logger.warning("Planner returned no chain for swap")
                continue

            available = CHAIN_MODULES.get(chain_name, [])
            if not available:
                logger.warning(f"No swap modules for {chain_name}")
                continue

            module = random.choice(available)

            chain = Chain(
                chain_name=chain_name,
                native_token=chain_mapping[chain_name].native_token,
                rpc=chain_mapping[chain_name].rpc,
                chain_id=chain_mapping[chain_name].chain_id,
                scan=chain_mapping[chain_name].scan
            )

            logger.info(f"Swap #{i+1}/{swaps_count}: {module} on {chain_name}")

            success = await self._run_with_retries(module, chain)

            self.memory.record_swap(chain_name, module, success)

            pause = random.randint(30, 120)
            logger.info(f"Pause between swaps: {pause}s")
            await asyncio.sleep(pause)

    async def _run_with_retries(self, module, chain, retries=3):
        for attempt in range(1, retries + 1):
            try:
                if await MODULE_HANDLERS[module](self.route, chain):
                    logger.success(f"{module} success on {chain.chain_name}")
                    return True
            except Exception as e:
                logger.warning(f"{module} retry {attempt}/{retries}: {e}")
        return False

