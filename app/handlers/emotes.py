from telethon import events

from app.utils.emotes_gif import get_gif
from app.utils.mention_getter import get_mentioned_user


async def init(bot):
    @bot.on(events.NewMessage(pattern="(?i)!? ?hug"))
    @bot.on(events.NewMessage(pattern="!? ?[оО][бБ][нН][яЯ][лЛ]"))
    @bot.on(events.NewMessage(pattern="!? ?[оО][бБ][нН][яЯ][тТ][ьЬ]"))
    async def handler(event):
        if event.is_group and event.mentioned:
            mention = await get_mentioned_user(event.message, event.client)
            sender = f"<a href=\"tg://user?id={event.sender.id}\">{event.sender.first_name}</a>"
            receiver = f"<a href=\"tg://user?id={mention.id}\">{mention.first_name}</a>"
            await event.reply(f"{sender} обнимает {receiver}", file=await get_gif("hug"), parse_mode="html")
