from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_quote_keyboard(quote: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Save Quote", callback_data=f"save_quote:{quote}")]
    ])
    return keyboard

def get_language_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="English", callback_data="lang:en")],
        [InlineKeyboardButton(text="Русский", callback_data="lang:ru")]
    ])
    return keyboard
