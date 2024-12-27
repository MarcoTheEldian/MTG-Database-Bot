import asyncio
from aiogram import Bot, Dispatcher
from aiohttp import web
from core.config import Config
from bot.handlers import start
from bot.handlers import help
from bot.handlers import find
from bot.handlers import inline_query

async def on_start(request):
    return web.Response(text="Webhook is working!")


async def main():
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(find.router)
    dp.include_router(inline_query.router)


    webhook_url = f"https://yourdomain.com/{Config.BOT_TOKEN}"

    # Настройка webhook на сервере
    await bot.set_webhook(webhook_url)

    # Настроим веб-сервер для обработки webhook-запросов
    app = web.Application()
    app.router.add_post(f'/{Config.BOT_TOKEN}', dp.start_webhook)

    # Запуск веб-сервера для получения обновлений через webhook
    try:
        print(f"Starting webhook server on https://yourdomain.com/{Config.BOT_TOKEN}")
        web.run_app(app, host='0.0.0.0', port=80)
    finally:
        await bot.session.close()

    if __name__ == "__main__":
        asyncio.run(main())