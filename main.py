from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Naruto=Client(
    "Imdb Bot",
    bot_token="5250937026:AAEveOUt5fOisEK7JD1ByjfOuNcLeX0bBus",
    api_id="15316155",
    api_hash="c2340e29da60393bc3c96fa7c0870911"
)


START_MESSAGE = """
start message


Description
"""





@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
  
     await message.reply_text(
         text=START_MESSAGE
     )
       
  

Naruto.run()
