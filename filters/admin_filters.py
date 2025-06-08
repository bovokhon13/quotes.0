from aiogram.filters import BaseFilter
from config.settings import ADMIN_IDS

class AdminFilter(BaseFilter):
    async def __call__(self, message):
        return message.from_user.id in ADMIN_IDS
