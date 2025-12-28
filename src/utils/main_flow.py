from src.utils.memory import GlobalMemory
from src.utils.planner import ActivityPlanner
from src.utils.bridges.bridge_executor import BridgeExecutor
from src.modules.swaps.swap_executor import SwapExecutor

memory = GlobalMemory()
planner = ActivityPlanner(memory)

# 1️⃣ Bridge day
await BridgeExecutor(route, planner, memory).run_bridge_day()

# 2️⃣ Swap day
await SwapExecutor(route, planner, memory.swaps).run_swap_day()


    # === BRIDGE DAY ===
    if memory_manager.can_bridge_today(route.wallet.address):
        await BridgeExecutor(
            route=route,
            planner=planner,
            memory=memory_manager
        ).run_bridge_day()

        memory_manager.remember_bridge_day(route.wallet.address)

    # === SWAP DAY ===
    await SwapExecutor(
        route=route,
        planner=planner,
        memory=activity_memory
    ).run_swap_day()
