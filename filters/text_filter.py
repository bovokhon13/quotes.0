from aiogram.filters import BaseFilter

class QuoteFilter(BaseFilter):
    async def __call__(self, message):
        return message.text.isdigit()
