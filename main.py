from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Naruto=Client(
    "Imdb Bot",
    bot_token="5203542667:AAHMeoeCAq3iVLrChuxXspJPHzg5H2CH8NM",
    api_id="15316155",
    api_hash="c2340e29da60393bc3c96fa7c0870911"
)




ALL_PIC = [
 "https://telegra.ph/file/13527c7b40976c1368cca.jpg",
 "https://telegra.ph/file/73ad5f7b9ac871d08d058.jpg",
 "https://telegra.ph/file/56e2c12ed686eeb4513da.jpg",
 "https://telegra.ph/file/7cde9e71ebffa93a0d209.jpg",
 "https://telegra.ph/file/cdd859489cae56263bd74.jpg"
]




@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
   await message.reply_photo(
       photo=random.choice(ALL_PIC),
       caption="𝙷𝙴𝚈 𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 𝙰 <a href='https://t.me/PyrogramTextBot'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙱𝙾𝚃</a> 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 𝙰𝙽𝙳 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 <a href='https://t.me/TEAM_KERALA'>𝚃𝚐 𝙵𝙻𝚄𝙵𝙵𝚈</a>",
       reply_markup=InlineKeyboardMarkup( [[
          ],[
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥", url="t.me/PR0FESS0R_99"),
          ]]

        )
        
     )
   

Naruto.run()
