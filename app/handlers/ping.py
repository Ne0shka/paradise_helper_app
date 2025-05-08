import time

from loguru import logger
from telethon import events


async def init(bot):
    @bot.on(events.NewMessage(pattern="(?i)!? ?ping"))
    @bot.on(events.NewMessage(pattern="!? ?[пП][иИ][нН][гГ]"))
    async def handler(event):
        snapshot = time.time()
        msg = await event.reply("✅ Понг!")
        delta = time.time() - snapshot
        await msg.edit(f"✅ Понг!\n⌛ {delta:.2f} сек.")
        logger.info(f"Пинг: {delta:.2f} сек.")
