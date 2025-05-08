import os

from loguru import logger
from dotenv import load_dotenv
from telethon import TelegramClient

from app import handlers
from app.utils import setup_logger


async def app_run():
    setup_logger.setup()
    logger.info("Инициализация бота...")
    load_dotenv()
    bot = TelegramClient(
        "bot",
        api_id=int(os.getenv("API_ID")),
        api_hash=os.getenv("API_HASH"),
    )
    try:
        await bot.start(bot_token=os.getenv("BOT_TOKEN"))
        await handlers.init(bot)
        logger.info("Бот в сети!")
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()
