planner = ActivityPlanner()
memory = ActivityMemory()

# 1️⃣ Бриджи
await BridgeExecutor(route, planner, memory).run_bridge_day()

# 2️⃣ Свапы (ОТДЕЛЬНО)
swap_executor = SwapExecutor(route, planner, memory)
await swap_executor.run_swap_day()

