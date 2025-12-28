import random
import asyncio
from loguru import logger

from src.models.chain import Chain
from src.utils.data.chains import chain_mapping
from src.utils.chain_modules import CHAIN_MODULES, MODULE_HANDLERS


async def process_swap_day(route, planner):
    logger.info("SWAP DAY started")

    num_swaps = planner.choose_swap_count()
    logger.info(f"Planning {num_swaps} swaps")

    for i in range(num_swaps):
        chain_name = planner.choose_swap_chain()
        if not chain_name:
            logger.warning("Planner returned no chain for swap")
            continue

        chain_obj = Chain.from_mapping(chain_mapping[chain_name])

        available_swaps = CHAIN_MODULES.get(chain_name, [])
        if not available_swaps:
            logger.warning(f"No swaps available for {chain_name}")
            continue

        swap_name = planner.choose_swap_module(available_swaps)

        logger.info(f"Swap #{i+1}/{num_swaps}: {swap_name} on {chain_name}")

        max_attempts = 5
        for attempt in range(1, max_attempts + 1):
            try:
                success = await MODULE_HANDLERS[swap_name](route, chain_obj)
                if success:
                    logger.success(f"Swap successful: {swap_name} on {chain_name}")
                    break
                else:
                    logger.warning(f"Swap failed: {swap_name} attempt {attempt}")
            except Exception as e:
                logger.error(f"Swap crashed: {e} attempt {attempt}")
        else:
            logger.warning(f"Swap skipped after {max_attempts} attempts")

        pause = planner.swap_pause()
        logger.info(f"Pause between swaps: {pause}s")
        await asyncio.sleep(pause)

    logger.info("SWAP DAY finished")
