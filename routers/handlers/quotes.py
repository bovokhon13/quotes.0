from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from services.api_client import fetch_quote
from storage.user_data import save_quote, get_quotes, delete_quote
from utils.locales import get_translation
from filters.text_filter import QuoteFilter
from keyboards.inline import get_quote_keyboard

router = Router()

class QuoteStates(StatesGroup):
    waiting_for_quote_index = State()

@router.message(Command("quote"))
async def cmd_quote(message: Message):
    quote = await fetch_quote()
    await message.answer(
        get_translation(message.from_user.language_code, "quote").format(quote=quote),
        reply_markup=get_quote_keyboard(quote)
    )

@router.message(Command("favorites"))
async def cmd_favorites(message: Message):
    quotes = await get_quotes(message.from_user.id)
    if not quotes:
        await message.answer(get_translation(message.from_user.language_code, "no_favorites"))
        return
    response = "\n".join(f"{i+1}. {quote}" for i, quote in enumerate(quotes))
    await message.answer(get_translation(message.from_user.language_code, "favorites").format(quotes=response))

@router.message(Command("delete_quote"))
async def cmd_delete_quote(message: Message, state: FSMContext):
    await message.answer(get_translation(message.from_user.language_code, "enter_quote_index"))
    await state.set_state(QuoteStates.waiting_for_quote_index)

@router.message(QuoteStates.waiting_for_quote_index, QuoteFilter())
async def process_quote_index(message: Message, state: FSMContext):
    try:
        index = int(message.text) - 1
        if await delete_quote(message.from_user.id, index):
            await message.answer(get_translation(message.from_user.language_code, "quote_deleted"))
        else:
            await message.answer(get_translation(message.from_user.language_code, "invalid_index"))
    except ValueError:
        await message.answer(get_translation(message.from_user.language_code, "invalid_input"))
    await state.clear()

@router.callback_query(F.data.startswith("save_quote:"))
async def save_quote_callback(callback: CallbackQuery):
    quote = callback.data.split(":", 1)[1]
    await save_quote(callback.from_user.id, quote)
    await callback.message.answer(get_translation(callback.from_user.language_code, "quote_saved"))
    await callback.answer()
