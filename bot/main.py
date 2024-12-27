import asyncio
from aiogram import Bot, Dispatcher
from core.config import Config
from bot.handlers import start
from bot.handlers import help
from bot.handlers import find
from bot.handlers import inline_query


async def main():
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(find.router)
    dp.include_router(inline_query.router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())