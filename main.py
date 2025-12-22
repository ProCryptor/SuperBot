from asyncio import run, set_event_loop_policy, gather, create_task, sleep
from typing import Awaitable
import random
import asyncio
import logging
import sys
import time

from loguru import logger
from termcolor import cprint
from rich.console import Console
from rich.panel import Panel
from rich import box
from config import *
from src.utils.data.helper import private_keys, proxies
from src.database.generate_database import generate_database
from src.database.models import init_models, engine
from src.utils.data.mappings import module_handlers
from src.utils.manage_tasks import manage_tasks
from src.utils.retrieve_route import get_routes
from src.models.route import Route
from src.models.chain import Chain
from src.utils.data.chains import chain_mapping
from src.utils.tg_app.telegram_notifications import TGApp

from src.ui.interface import get_module, LOGO_LINES, PROJECT_INFO, clear_screen, get_module_menu

# Настройка логгеров
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.CRITICAL)

if sys.platform == 'win32':
    set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

console = Console()

async def process_task(routes: list[Route]) -> None:
    if not routes:
        logger.success('All tasks are completed')
        return

    wallet_tasks = []
    for route in routes:
        wallet_tasks.append(create_task(process_route(route)))

        time_to_pause = random.randint(PAUSE_BETWEEN_WALLETS[0], PAUSE_BETWEEN_WALLETS[1]) \
            if isinstance(PAUSE_BETWEEN_WALLETS, list) else PAUSE_BETWEEN_WALLETS
        logger.info(f'Sleeping for {time_to_pause} seconds before next wallet...')
        await sleep(time_to_pause)

    await gather(*wallet_tasks)

async def process_route(route: Route) -> None:
    # 25% дней — кошелек ничего не делает (человеческое поведение)
    if random.random() < 0.25:
        logger.info(f'Wallet {route.wallet.address} skips activity today')
        return

async def process_route(route: Route) -> None:
    if route.wallet.proxy:
        if route.wallet.proxy.proxy_url and MOBILE_PROXY and ROTATE_IP:
            await route.wallet.proxy.change_ip()

    private_key = route.wallet.private_key

    module_tasks = []
    for task in route.tasks:

    # 20% шанс пропустить задачу
    if random.random() < 0.2:
        logger.info(f'Skipping task {task} (human randomness)')
        continue

        module_tasks.append(create_task(process_module(task, route, private_key)))

        random_sleep = random.randint(PAUSE_BETWEEN_MODULES[0], PAUSE_BETWEEN_MODULES[1]) if isinstance(
            PAUSE_BETWEEN_MODULES, list) else PAUSE_BETWEEN_MODULES

        logger.info(f'Sleeping for {random_sleep} seconds before next module...')
        await sleep(random_sleep)
        # 10% шанс долгой паузы (человек отвлёкся)
    if random.random() < 0.1:
        long_sleep = random.randint(300, 1800)
        logger.info(f'Long human pause: {long_sleep} seconds')
        await sleep(long_sleep)

    await gather(*module_tasks)

    # if TG_BOT_TOKEN and TG_USER_ID:
       # tg_app = TGApp(
            # token=TG_BOT_TOKEN,
            # tg_id=TG_USER_ID,
            # private_key=private_key
        )
        # await tg_app.send_message()

async def process_module(task: str, route: Route, private_key: str, chain_name: str = "BASE") -> None:
    chain = Chain(
        chain_name=chain_name,
        native_token=chain_mapping[chain_name].native_token,
        rpc=chain_mapping[chain_name].rpc,
        chain_id=chain_mapping[chain_name].chain_id
    )
    completed = await module_handlers[task](route, chain)
    if completed:
        await manage_tasks(private_key, task)

from src.ui.interface import get_module, clear_screen, LOGO_LINES, PROJECT_INFO

async def main_loop() -> None:
    clear_screen()  # очищаем экран только один раз при первом запуске
    for line in LOGO_LINES:
        console.print(line, justify="center")
    console.print(PROJECT_INFO, justify="center")

    await init_models(engine)

    while True:
        time.sleep(0.3)
        module = get_module_menu()

        if module == 3:
            logger.info("Exiting the program...")
            break

        if module == 1:
            if SHUFFLE_WALLETS:
                random.shuffle(private_keys)

            logger.debug("Generating new database")
            await generate_database(engine, private_keys, proxies)

        elif module == 2:
            logger.debug("Working with the database")
            routes = await get_routes(private_keys)
            await process_task(routes)

        else:
            logger.error("Invalid choice")


def start_event_loop(awaitable: Awaitable[None]) -> None:
    run(awaitable)

if __name__ == '__main__':
    try:
        start_event_loop(main_loop())
    except KeyboardInterrupt:
        cprint(f'\nQuick software shutdown', color='light_yellow')
        sys.exit()
