from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline import get_language_keyboard
from utils.locales import get_translation

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(get_translation(message.from_user.language_code, "welcome"))

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(get_translation(message.from_user.language_code, "help"))

@router.message(Command("language"))
async def cmd_language(message: Message):
    await message.answer(
        get_translation(message.from_user.language_code, "choose_language"),
        reply_markup=get_language_keyboard()
    )
