from src.utils.memory import MemoryManager, ActivityMemory
from src.utils.planner import ActivityPlanner
from src.modules.bridges.bridge_executor import BridgeExecutor
from src.modules.swaps.swap_executor import SwapExecutor


async def main_flow(route):
    """
    Главный сценарий активности аккаунта
    """

    # === ПАМЯТЬ ===
    memory_manager = MemoryManager()
    activity_memory = ActivityMemory()

    # === ПЛАНИРОВЩИК ===
    planner = ActivityPlanner(
        memory=activity_memory,
        global_memory=memory_manager
    )

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
