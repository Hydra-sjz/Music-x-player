from pyrogram import filters
from pyrogram.types import Message

from PROFESSOR import app
from PROFESSOR.core.call import PROF
from PROFESSOR.utils.database import set_loop
from PROFESSOR.utils.decorators import AdminRightsCheck
from PROFESSOR.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await PROF.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"], reply_markup=close_markup(_)
    )

#.format(message.from_user.mention)
