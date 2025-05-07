import time

from telethon import events


async def init(bot):
    @bot.on(events.NewMessage(pattern="![пП]инг"))
    async def handler(e):
        s = time.time()
        m = await e.reply("✅ Понг!")
        d = time.time() - s
        await m.edit(f"✅ Понг!\n⌛ {d:.2f} сек.")
