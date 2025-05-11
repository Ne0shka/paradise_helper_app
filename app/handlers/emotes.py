from telethon import events

from app.services.emotes_gif import get_gif
from app.services.mention_getter import get_mentioned_user


async def init(bot):  # FIXME: REFACTOR
    @bot.on(events.NewMessage(pattern="(?i)!? ?hug"))
    @bot.on(events.NewMessage(pattern="!? ?[оО][бБ][нН][яЯ][лЛ]"))
    @bot.on(events.NewMessage(pattern="!? ?[оО][бБ][нН][яЯ][тТ][ьЬ]"))
    async def handler(event):
        if event.is_group:
            sender = f"<a href=\"tg://user?id={event.sender.id}\">{event.sender.first_name}</a>"
            mention = await get_mentioned_user(event.message, event.client)
            if mention is not None:
                receiver = f"<a href=\"tg://user?id={mention.id}\">{mention.first_name}</a>"
            elif event.is_reply:
                reply_user = (await event.get_reply_message()).sender
                receiver = f"<a href=\"tg://user?id={reply_user.id}\">{reply_user.first_name}</a>"
            else:
                return
            await event.reply(f"{sender} обнимает {receiver}", file=await get_gif("hug"), parse_mode="html")

    @bot.on(events.NewMessage(pattern="(?i)!? ?kiss"))
    @bot.on(events.NewMessage(pattern="!? ?([цЦ]|[тТ][ьЬ])[мМ][оО][кК]"))
    @bot.on(events.NewMessage(pattern="!? ?[пП][оО][цЦ][еЕ][лЛ][оО][вВ][аА][лЛ]"))
    @bot.on(events.NewMessage(pattern="!? ?[пП][оО][цЦ][еЕ][лЛ][оО][вВ][аА][тТ][ьЬ]"))
    async def handler(event):
        if event.is_group:
            sender = f"<a href=\"tg://user?id={event.sender.id}\">{event.sender.first_name}</a>"
            mention = await get_mentioned_user(event.message, event.client)
            if mention is not None:
                receiver = f"<a href=\"tg://user?id={mention.id}\">{mention.first_name}</a>"
            elif event.is_reply:
                reply_user = (await event.get_reply_message()).sender
                receiver = f"<a href=\"tg://user?id={reply_user.id}\">{reply_user.first_name}</a>"
            else:
                return
            await event.reply(f"{sender} целует {receiver}", file=await get_gif("kiss"), parse_mode="html")

    @bot.on(events.NewMessage(pattern="(?i)!? ?bite"))
    @bot.on(events.NewMessage(pattern="!? ?[кК][уУ][сС][ьЬ]"))
    @bot.on(events.NewMessage(pattern="!? ?[уУ][кК][уУ][сС][иИ][лЛ]"))
    @bot.on(events.NewMessage(pattern="!? ?[уУ][кК][уУ][сС][иИ][тТ][ьЬ]"))
    async def handler(event):
        if event.is_group:
            sender = f"<a href=\"tg://user?id={event.sender.id}\">{event.sender.first_name}</a>"
            mention = await get_mentioned_user(event.message, event.client)
            if mention is not None:
                receiver = f"<a href=\"tg://user?id={mention.id}\">{mention.first_name}</a>"
            elif event.is_reply:
                reply_user = (await event.get_reply_message()).sender
                receiver = f"<a href=\"tg://user?id={reply_user.id}\">{reply_user.first_name}</a>"
            else:
                return
            await event.reply(f"{sender} кусает {receiver}", file=await get_gif("bite"), parse_mode="html")
