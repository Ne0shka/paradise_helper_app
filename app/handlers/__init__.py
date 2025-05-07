# Пример взят отсюда: https://github.com/Lonami/TelethonianBotExt/blob/master/__init__.py
import os
import asyncio
import importlib


async def init(bot):
    handlers = [
        importlib.import_module(".", f"{__name__}.{file[:-3]}")

        for file in os.listdir(os.path.dirname(__file__))

        if file.endswith(".py") and file[0].isalnum()
    ]
    to_init = (_init_handler(handler, bot) for handler in handlers)
    await asyncio.gather(*(filter(None, to_init)))


async def _init_handler(handler, bot):
    h_init = getattr(handler, "init",  None)
    if not callable(h_init):
        return
    try:
        hname = handler.__name__.split(".")[-1]
        print("Загрузка модуля", hname, "...")
        h_init = await handler.init(bot)
        print("Модуль", hname, "успешно загружен!")
    except Exception:
        print("Ошибка загрузки модуля", handler)
    else:
        if asyncio.iscoroutine(h_init):
            await h_init
