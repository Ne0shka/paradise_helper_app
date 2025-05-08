import asyncio

from app.bot import app_run


if __name__ == "__main__":
    try:
        asyncio.run(app_run())
    except (KeyboardInterrupt, SystemExit):
        print("Завершение работы...")
