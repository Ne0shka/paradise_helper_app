import time

from loguru import logger
from telethon import events


async def init(bot):
    @bot.on(events.NewMessage(pattern="(?i)!? ?ping"))
    @bot.on(events.NewMessage(pattern="!? ?[пП][иИ][нН][гГ]"))
    async def handler(msg):
        snapshot = time.time()
        reply = await msg.reply("✅ Понг!")
        delta = time.time() - snapshot
        await reply.edit(f"✅ Понг!\n⌛ {delta:.2f} сек.")
        logger.info(f"Пинг: {delta:.2f} сек.")
