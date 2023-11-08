import datetime

import requests
from aiogram import types

from core.bot import bot
from core.db import CurrencyHistory, Subscriber, session


async def send_currency_rate(message: types.Message):
    usd_to_rub = await get_exchange_rate()
    await process_currency_rate(message.chat.id, usd_to_rub)


async def send_currency_rate_to_subscribers():
    usd_to_rub = await get_exchange_rate()
    subscribers = session.query(Subscriber).all()
    for subscriber in subscribers:
        chat_id = subscriber.chat_id
        await process_currency_rate(chat_id, usd_to_rub)


async def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    usd_to_rub = data['rates']['RUB']
    return usd_to_rub


async def process_currency_rate(chat_id, usd_rate):
    if usd_rate is not None:
        await bot.send_message(chat_id=chat_id, text=f"Текущий курс доллара к рублю: {usd_rate}")
        history = CurrencyHistory(user_id=chat_id, date=datetime.datetime.now(), currency_rate=usd_rate)
        session.add(history)
        session.commit()
    else:
        await bot.send_message(chat_id=chat_id, text="Не удалось получить курс доллара.")


async def history_command(message: types.Message):
    """
    Отправляет историю курса доллара.

    """
    history = session.query(CurrencyHistory).filter_by(user_id=message.chat.id).all()
    if history:
        result = "История курса доллара:\n"
        for item in history:
            result += f"Дата: {item.date}, Курс: {item.currency_rate}\n"
        await message.answer(result)
    else:
        await message.answer("История пуста.")


async def unsubscribe_command(message: types.Message):
    """
    Отписывает пользователя от получения курса доллара.

    """
    subscriber = session.query(Subscriber).filter_by(chat_id=message.chat.id).first()
    if subscriber:
        session.delete(subscriber)
        session.commit()
        await message.answer("Вы успешно отменили подписку на получение курса доллара.")
    else:
        await message.answer("Вы не подписаны на получение курса доллара.")


async def subscribe_command(message: types.Message):
    """
    Подписывает пользователя на получение курса доллара.

    """
    subscriber = session.query(Subscriber).filter_by(chat_id=message.chat.id).first()
    if subscriber is None:
        subscriber = Subscriber(chat_id=message.chat.id)
        session.add(subscriber)
        session.commit()
        await message.answer("Вы успешно подписались на получение курса доллара.")
    else:
        await message.answer("Вы уже подписаны на получение курса доллара.")
