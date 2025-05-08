from telethon.tl.types import MessageEntityMention, MessageEntityMentionName


async def get_mentioned_user(msg, cl):
    for e in msg.entities:
        if type(e) == MessageEntityMention:
            username = msg.message[e.offset:e.offset+e.length]
            return await cl.get_entity(username)
        if type(e) == MessageEntityMentionName:
            return await cl.get_entity(e.user_id)
