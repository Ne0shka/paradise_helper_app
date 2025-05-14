from aiohttp import ClientSession

from app.services.mention_getter import get_mentioned_user, get_mention_link


async def get_targets(event):
    sender = await get_mention_link(event.sender)
    mention = await get_mentioned_user(event)
    if mention is not None:
        receiver = await get_mention_link(mention)
        return sender, receiver
    elif event.is_reply:
        receiver = await get_mention_link((await event.get_reply_message()).sender)
        return sender, receiver
    else:
        return None, None


async def get_gif(emote):
    async with ClientSession("https://api.otakugifs.xyz") as session:
        async with session.get("/gif", params={"reaction": emote}) as resp:
            return (await resp.json())["url"]