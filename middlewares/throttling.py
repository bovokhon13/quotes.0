from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache
import asyncio

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache = TTLCache(maxsize=10000, ttl=5)

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        if user_id in self.cache:
            await event.answer("Пожалуйста, подождите несколько секунд перед отправкой следующего сообщения.")
            return
        self.cache[user_id] = True
        return await handler(event, data)
