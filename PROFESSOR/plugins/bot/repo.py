from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PROFESSOR import app
from config import BOT_USERNAME

start_txt = """
⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ sᴏᴜʀᴀʙʜ ʀᴇᴘᴏs ⌾

◎ ʙʜᴀɢ ʙʜᴏsᴅɪᴋᴇ

◎ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ ʀᴀɴᴅɪ ᴋᴇ.

◎ ʀᴇᴘᴏ ᴛᴏ ɴᴀ ᴅᴜɴɢᴀ.
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ＡＤＤ ＭＥ ＢＡＢＹ ⦿", url=f"https://t.me/Professor_Sukoon_Bot?startgroup=True&admin=delete_messages+invite_users+pin_messages")
        ],
        [
          InlineKeyboardButton("⦿ ʜᴇʟᴘ ⦿", url="https://t.me/Friends_Chatting_Masti_Group"),
          InlineKeyboardButton("⦿ ᴘʀᴏғᴇssᴏʀ ⦿", url="https://t.me/II_PROFESSOR_SOURABH_II"),
          ],
               [
                InlineKeyboardButton("⦿ ᴘʀᴏғᴇssᴏʀ ɴᴇᴛᴡᴏʀᴋ ⦿", url="https://t.me/PROFESSOR_NETWORK"),

],
[
              InlineKeyboardButton("⦿ ᴍᴀɪɴ ʙᴏᴛ ⦿", url=f"https://t.me/Professor_Sukoon_Bot"),
              InlineKeyboardButton("︎⦿ ᴍʏ ʀᴇᴘᴏ ⦿", url=f"https://t.me/PrivateBotRepo"),
       
    ],
    [
              InlineKeyboardButton("⦿ sᴛʀɪɴɢ ɢᴇɴ ⦿", url=f"https://t.me/String_Generate_op_bot"),
              InlineKeyboardButton("︎⦿ sᴛʀɪɴɢ ʜᴀᴄᴋ ⦿", url=f"https://t.me/ProfessorStringHackRobot"),
       
    ],
    [ 
          InlineKeyboardButton("⦿ ᴊᴏɪɴ ғᴏʀ sᴘᴀᴍ ʙᴏᴛ sᴜᴅᴏ ⦿", url=f"https://t.me/PROFESSOR_SANATANI")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/c0347afa461151285cef5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
