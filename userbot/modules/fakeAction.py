from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake Typing For {t} sec.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake audio recording For {t} sec.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake video recording For {t} sec.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake Game Playing For {t} sec.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)

CMD_HELP.update({
    "fakeaction":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .ftyping <text count>\
   \nUsage : As if you're typing when you're not\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .faudio <text count>\
   \nUsage : Works the same as ftyping but this is in the form of fake audio\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .fgame <text count>\
   \nUsage : Works the same as ftyping but this is in the form of a fake game\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .fvideo <text count>\
   \nUsage : Works the same as ftyping but this is in the form of a fake video"
})
