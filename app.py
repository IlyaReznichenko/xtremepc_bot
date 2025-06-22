import asyncio

import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from fastapi import FastAPI

from routers.configurator import configurator_router
from src.core.logging import logger
from src.middlewares.subscription import CheckSubscription
from src.routers.base import base_router
from src.schemas.base import config

app = FastAPI()


async def main() -> None:
    """Корутина для запуска основноого бота"""
    bot = Bot(
        token=config.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Подключение роутеров к проекту
    dp.include_routers(
        base_router,
        configurator_router
    )

    dp.message.middleware(CheckSubscription())
    
    await bot.delete_webhook(True)
    await dp.start_polling(bot)

async def start_fastapi():
    conf = uvicorn.Config(app, host=config.FASTAPI_HOST, port=config.FASTAPI_PORT)
    server = uvicorn.Server(conf)
    await server.serve()


async def run_app():
    await asyncio.gather(main(), start_fastapi())


if __name__ == "__main__":
    logger.info('Запуск бота')
    asyncio.run(run_app())

