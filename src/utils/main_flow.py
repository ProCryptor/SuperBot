from src.utils.memory import MemoryManager, ActivityMemory

memory = MemoryManager()          # для chain/bridge/tasks
activity_memory = ActivityMemory()  # для swaps

planner = ActivityPlanner(memory, activity_memory)  

await BridgeExecutor(route, planner, memory).run_bridge_day()
await SwapExecutor(route, planner, activity_memory).run_swap_day()  
