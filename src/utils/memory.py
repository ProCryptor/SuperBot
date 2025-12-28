from collections import defaultdict
from datetime import datetime, timedelta


class MemoryManager:
    def __init__(self):
        self.last_chain = {}
        self.last_bridge_day = {}
        self.recent_tasks = defaultdict(list)

    # ===== CHAINS =====
    def remember_chain(self, wallet: str, chain: str):
        self.last_chain[wallet] = chain

    def get_last_chain(self, wallet: str):
        return self.last_chain.get(wallet)

    # ===== BRIDGES =====
    def remember_bridge(self, wallet: str):
        self.last_bridge_day[wallet] = datetime.utcnow()

    def can_bridge_today(self, wallet: str, cooldown_days: int = 2) -> bool:
        last = self.last_bridge_day.get(wallet)
        if not last:
            return True
        return datetime.utcnow() - last > timedelta(days=cooldown_days)

    # ===== TASKS =====
    def remember_task(self, wallet: str, task: str, limit: int = 5):
        self.recent_tasks[wallet].append(task)
        self.recent_tasks[wallet] = self.recent_tasks[wallet][-limit:]

    def was_task_recent(self, wallet: str, task: str) -> bool:
        return task in self.recent_tasks[wallet]
# src/utils/memory.py
from collections import defaultdict
import time


class ActivityMemory:
    def __init__(self):
        self.last_chain = None

        self.failed_swaps = defaultdict(int)   # (chain, module) -> count
        self.success_swaps = defaultdict(int)

        self.recent_swaps = []  # [(chain, module, ts)]

    # ===== SWAPS =====

    def record_swap(self, chain, module, success: bool):
        key = (chain, module)

        if success:
            self.success_swaps[key] += 1
        else:
            self.failed_swaps[key] += 1

        self.recent_swaps.append((chain, module, time.time()))
        self.recent_swaps = self.recent_swaps[-20:]  # ограничение памяти

    def swap_failed_too_much(self, chain, module, limit=3) -> bool:
        return self.failed_swaps[(chain, module)] >= limit

    def was_recent_swap(self, chain, module, window=3600) -> bool:
        now = time.time()
        return any(
            c == chain and m == module and now - ts < window
            for c, m, ts in self.recent_swaps
        )

    # ===== CHAINS =====

    def update_chain(self, chain):
        self.last_chain = chain
