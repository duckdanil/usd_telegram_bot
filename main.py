from aiogram.utils import executor

from core.bot import dp
from core.scheduler import on_startup, on_shutdown
from core.handlers import start_handler,subscribe_handler,send_currency_rate,unsubscribe_handler,history_handler

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)