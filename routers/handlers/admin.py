from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from filters.admin_filter import AdminFilter
from utils.locales import get_translation
import aiofiles
import json

router = Router()

@router.message(Command("stats"), AdminFilter())
async def cmd_stats(message: Message):
    async with aiofiles.open("storage/user_data.json", "r") as f:
        data = json.loads(await f.read() or "{}")
    total_users = len(data)
    total_quotes = sum(len(quotes) for quotes in data.values())
    await message.answer(
        get_translation(message.from_user.language_code, "stats").format(
            users=total_users, quotes=total_quotes
        )
    )
