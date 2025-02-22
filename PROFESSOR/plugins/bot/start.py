import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from PROFESSOR import app
from PROFESSOR.misc import _boot_
from PROFESSOR.plugins.sudo.sudoers import sudoers_list
from PROFESSOR.utils.database import get_served_chats, get_served_users, get_sudoers
from PROFESSOR.utils import bot_sys_stats
from PROFESSOR.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from PROFESSOR.utils.decorators.language import LanguageStart
from PROFESSOR.utils.formatters import get_readable_time
from PROFESSOR.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



NEXI_VID = [
"https://telegra.ph/file/6ae3a399b96f70b6fda79.mp4",
"https://telegra.ph/file/5df37a776933bb427b528.mp4",
"https://telegra.ph/file/85a35e5a79525b70f5904.mp4",
"https://telegra.ph/file/75764b093a76d08f51d2c.mp4",
"https://telegra.ph/file/ea951700bb21f53df70c9.mp4",
"https://telegra.ph/file/b74553a355a110d9a016b.mp4",
"https://telegra.ph/file/959dc8b67413e50f1c4a5.mp4",
"https://graph.org/file/2a7f857f31b32766ac6fc.mp4",
"https://graph.org/file/83ebf52e8bbf138620de7.mp4",
"https://graph.org/file/ba7699c28dab379b518ca.mp4",

]

PHOTO = [
"https://telegra.ph/file/cdef188e7da67a40f9c73.jpg",
"https://telegra.ph/file/5f1b792642f8f7f051b5a.jpg",
"https://telegra.ph/file/badb5f475832923d7d4b4.jpg",
"https://telegra.ph/file/049ea9201b95db1b853e9.jpg",
"https://telegra.ph/file/4822b1159595027a0e259.jpg",
"https://telegra.ph/file/bbb36d4186c6536a2a41b.jpg",
"https://telegra.ph/file/5c5b15425c662b70ea2a6.jpg",
"https://telegra.ph/file/4eb5b032c051ec7a7942b.jpg",
"https://telegra.ph/file/f27786a08bedec9ca52cb.jpg",
]


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(PHOTO),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} Just started the bot to check<b>Sudolist</b>.\n\n<b>× User id</b> <code>{message.from_user.id}</code>\n<b>× User name:</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(

chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} Just started bot to check<b>Track information</b>.\n\n× <b>User id:</b> <code>{message.from_user.id}</code>\n× <b>User name:</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await message.reply_photo(
            random.choice(PHOTO),
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} Just started the bot.\n\n× <b>User id:</b> <code>{message.from_user.id}</code>\n× <b>User name:</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(PHOTO),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_text(
                    caption=_["start_3"].format(
                        app.mention,
                        message.chat.title,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
