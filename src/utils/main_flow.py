planner = ActivityPlanner()
memory = ActivityMemory()

# 1️⃣ Бриджи
await process_chain_disperse(route)

# 2️⃣ Свапы (ОТДЕЛЬНО)
swap_executor = SwapExecutor(route, planner, memory)
await swap_executor.run_swap_day()

