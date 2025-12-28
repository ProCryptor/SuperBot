from collections import defaultdict
from datetime import datetime, timedelta
import time


# ============================================================
# HIGH-LEVEL MEMORY (wallet / days / bridges / chains)
# ============================================================

class MemoryManager:
    """
    Долгоживущая память аккаунта.
    Используется мостами и главным флоу.
    """

    def __init__(self):
        self.last_chain: dict[str, str] = {}
        self.last_bridge_day: dict[str, datetime] = {}
        self.recent_tasks: dict[str, list[str]] = defaultdict(list)

    # ===== CHAINS =====

    def remember_chain(self, wallet: str, chain: str):
        self.last_chain[wallet] = chain

    def get_last_chain(self, wallet: str) -> str | None:
        return self.last_chain.get(wallet)

    # ===== BRIDGES =====

    def remember_bridge_day(self, wallet: str):
        self.last_bridge_day[wallet] = datetime.utcnow()

    def can_bridge_today(self, wallet: str, cooldown_days: int = 2) -> bool:
        last = self.last_bridge_day.get(wallet)
        if not last:
            return True
        return datetime.utcnow() - last > timedelta(days=cooldown_days)

    # ===== TASKS (generic anti-repeat) =====

    def remember_task(self, wallet: str, task: str, limit: int = 5):
        self.recent_tasks[wallet].append(task)
        self.recent_tasks[wallet] = self.recent_tasks[wallet][-limit:]

    def was_task_recent(self, wallet: str, task: str) -> bool:
        return task in self.recent_tasks[wallet]


# ============================================================
# ACTIVITY-LEVEL MEMORY (swaps, retries, failures)
# ============================================================

class ActivityMemory:
    """
    Оперативная память активности (swap day).
    Используется planner + swap executor.
    """

    def __init__(self):
        self.last_chain: str | None = None

        self.failed_swaps = defaultdict(int)     # (chain, module) -> count
        self.success_swaps = defaultdict(int)

        self.recent_swaps: list[tuple[str, str, float]] = []

    # ===== SWAPS =====

    def record_swap(self, chain: str, module: str, success: bool):
        key = (chain, module)

        if success:
            self.success_swaps[key] += 1
        else:
            self.failed_swaps[key] += 1

        self.recent_swaps.append((chain, module, time.time()))
        self.recent_swaps = self.recent_swaps[-30:]

    def swap_failed_too_much(self, chain: str, module: str, limit: int = 3) -> bool:
        return self.failed_swaps[(chain, module)] >= limit

    def was_recent_swap(self, chain: str, module: str, window: int = 3600) -> bool:
        now = time.time()
        return any(
            c == chain and m == module and now - ts < window
            for c, m, ts in self.recent_swaps
        )

    # ===== CHAINS =====

    def update_chain(self, chain: str):
        self.last_chain = chain
