from aiohttp import ClientSession


async def get_gif(emote):
    params = {"reaction": emote}
    async with ClientSession("https://api.otakugifs.xyz") as session:
        async with session.get("/gif",
                               params=params) as resp:
            return (await resp.json())["url"]