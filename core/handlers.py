from aiogram import types

from core.bot import dp
from core.functions import history_command, unsubscribe_command, subscribe_command, send_currency_rate


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    commands_message = """Доступные команды:
    /send_usd_rate - запросить текущий курс доллара
    /subscribe - подписаться на получение курса доллара
    /unsubscribe - отписаться от получения курса доллара
    /history - просмотреть историю ваших запросов курса доллара"""
    await message.answer(commands_message)


@dp.message_handler(commands=['send_usd_rate'])
async def send_usd_rate_handler(message: types.Message):
    await send_currency_rate(message)


@dp.message_handler(commands=['subscribe'])
async def subscribe_handler(message: types.Message):
    await subscribe_command(message)


@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe_handler(message: types.Message):
    await unsubscribe_command(message)


@dp.message_handler(commands=['history'])
async def history_handler(message: types.Message):
    await history_command(message)
