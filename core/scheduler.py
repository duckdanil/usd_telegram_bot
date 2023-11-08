from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import SCHEDULER_INTERVAL_SECONDS
from core.functions import send_currency_rate_to_subscribers

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
scheduler.add_job(send_currency_rate_to_subscribers, trigger='interval', seconds=SCHEDULER_INTERVAL_SECONDS)


async def on_startup(dp):
    scheduler.start()


async def on_shutdown(dp):
    scheduler.shutdown()
