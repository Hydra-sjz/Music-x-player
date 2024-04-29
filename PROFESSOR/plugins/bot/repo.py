from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PROFESSOR import app
from config import BOT_USERNAME

start_txt = """
✦ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ  ᴘʀᴏғᴇssᴏʀ sᴏᴜʀᴀʙʜ ʀᴇᴘᴏs !

✦ ᴍᴇʀᴀ ʟᴀɴᴅ ʟᴇ ʟᴇ༗

✦ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ ʀᴀɴᴅɪ ᴋᴇ.

✦ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ༗.
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＡＤＤ ＭＥ ＢＡＢＹ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("ＰＲＯＦＥＳＳＯＲ", url="https://t.me/SOURABH_OWNER"),
          ],
               [
                InlineKeyboardButton("ＰＲＯＦＥＳＳＯＲ ＮＥＴＷＯＲＫ", url="https://t.me/PROFESSOR_NETWORK"),

],
[
              InlineKeyboardButton("ＭＡＩＮ ＢＯＴ", url=f"https://t.me/Professor_Sukoon_Bot"),
              InlineKeyboardButton("︎ＭＹ ＲＥＰＯ", url=f"https://t.me/PROFESSORS_NETWORK"),
       
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/205f3cf027a5a11f5f70e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
