import os
import asyncio

from dotenv import load_dotenv
from telethon import TelegramClient

from app import handlers


async def main():
    print("Инициализация бота...")
    load_dotenv()
    bot = TelegramClient(
        "bot",
        api_id=int(os.getenv("API_ID")),
        api_hash=os.getenv("API_HASH"),
    )
    try:
        await bot.start(bot_token=os.getenv("BOT_TOKEN"))
        await handlers.init(bot)
        print("Бот в сети!")
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Завершение работы...")
