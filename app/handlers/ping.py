import time

from telethon import events


async def init(bot):
    @bot.on(events.NewMessage(pattern="(?i)!? ?ping"))
    async def handler(e):
        s = time.time()
        m = await e.reply("✅ Pong!")
        d = time.time() - s
        await m.edit(f"✅ Pong!\n⌛ {d:.2f}s")

    @bot.on(events.NewMessage(pattern="!? ?[пП][иИ][нН][гГ]"))
    async def handler(e):
        s = time.time()
        m = await e.reply("✅ Понг!")
        d = time.time() - s
        await m.edit(f"✅ Понг!\n⌛ {d:.2f} сек.")
