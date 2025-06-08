import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from routers import commands, quotes, admin
from middlewares.throttling import ThrottlingMiddleware
from utils.logger import setup_logger

async def main():
    setup_logger()
    logging.info("Starting Quote Bot...")
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Регистрация middleware
    dp.message.middleware(ThrottlingMiddleware())
    
    # Регистрация роутеров
    dp.include_router(commands.router)
    dp.include_router(quotes.router)
    dp.include_router(admin.router)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
