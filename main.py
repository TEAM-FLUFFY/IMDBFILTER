from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Rejaputh=Client(
      "pushpaBOT",
      bot_token="5250937026:AAEveOUt5fOisEK7JD1ByjfOuNcLeX0bBus",
      api_id="15316155",
      api_hash="c2340e29da60393bc3c96fa7c0870911",
)


ALL_PIC = [
 "https://telegra.ph/file/e3ec540aa3cc17c76850e.jpg",
 "https://telegra.ph/file/f24a2760d0392c88cc9e2.jpg",
 "https://telegra.ph/file/8bde50bae8dfd421022e5.jpg",
 "https://telegra.ph/file/ca52686ef7b66b3fca247.jpg"
]

@Rejaputh.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption="എന്റെ പേര് <a href=https://t.me/Pp_bp_RejuBot>𝕻𝖚𝖘𝖍𝖕𝖆</a>, 🔰മച്ചാനെ എന്റെ പണി കഴിഞ്ഞിട്ടില്ല അതുകൊണ്ട് RePo✅️ പ്രൈവറ്റ് ആണ് Work കഴിഞ്ഞിട്ട് public ആക്കും ",
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("🗨️𝐆𝐑𝐎𝐔𝐏🗨️", url="t.me/crimebhavanireju"),
          InlineKeyboardButton ("📂𝐂𝐇𝐀𝐍𝐍𝐄𝐋📂", url="t.me/updatechannel_forcrime"),
          ],[
          InlineKeyboardButton ("🔰𝐑𝐄𝐏𝐎 𝐄𝐃𝐈𝐓𝐙🔰", url="t.me/pushpa_Reju"),
          InlineKeyboardButton ("©️𝗕𝗢𝗧 𝗘𝗗𝗜𝗧𝗭", url="t.me/pushpa_Reju"),
          ],[
          InlineKeyboardButton ("👨‍💻𝗗𝗘𝗩👨‍💻", url="t.me/pushpa_Reju"),
          InlineKeyboardButton ("🟡𝕭𝖗𝖔𝖙𝖍𝖊𝖗𝕭𝖔𝖙🟡", url="t.me/IT_BUT_BOT"),
          ],[
          InlineKeyboardButton ("𝐑𝐄𝐏𝐎♂️", url="https://github.com/TG-chembanreju/pushpaBOT"),
          ]]
          )
          
        )
    
           
           
       
     
           
          

Narutu.run()
