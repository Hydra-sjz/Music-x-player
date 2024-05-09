from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PROFESSOR import app
from config import BOT_USERNAME

start_txt = """
✦ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ  ᴘʀᴏғᴇssᴏʀ sᴏᴜʀᴀʙʜ ʀᴇᴘᴏs !

✦ ᴍᴇʀᴀ ʀᴇᴘᴏ ʟᴇ ᴏʀ ʙʜᴀᴀɢ ᴊᴀʟᴅɪ

✦ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ ʀᴀɴᴅɪ ᴋᴇ.

✦ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ.
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＡＤＤ ＭＥ ＢＡＢＹ", url=f"https://t.me/Professor_Sukoon_Bot?startgroup=True&admin=delete_messages+invite_users+pin_messages")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("ᴘʀᴏғᴇssᴏʀ", url="https://t.me/SOURABH_OWNER"),
          ],
               [
                InlineKeyboardButton("ᴘʀᴏғᴇssᴏʀ ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/PROFESSOR_NETWORK"),

],
[
              InlineKeyboardButton("ᴍᴀɪɴ ʙᴏᴛ", url=f"https://t.me/Professor_Sukoon_Bot"),
              InlineKeyboardButton("︎ᴍʏ ʀᴇᴘᴏ ", url=f"https://github.com/PROFESSOR-SOURABH/PROFESSOR-MUSIC"),
       
    ],
    [
              InlineKeyboardButton("sᴛʀɪɴɢ ɢᴇɴ", url=f"https://t.me/String_Generate_op_bot"),
              InlineKeyboardButton("︎sᴛʀɪɴɢ ʜᴀᴄᴋ", url=f"https://t.me/ProfessorStringHackBot"),
       
    ],
    [ 
          InlineKeyboardButton("ᴊᴏɪɴ ғᴏʀ sᴘᴀᴍ ʙᴏᴛ sᴜᴅᴏ", url=f"https://t.me/PROFESSOR_SANATANI")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/205f3cf027a5a11f5f70e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
