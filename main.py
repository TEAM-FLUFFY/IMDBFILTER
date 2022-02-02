from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Naruto=Client(
    "Imdb Bot",
    bot_token="5250937026:AAEveOUt5fOisEK7JD1ByjfOuNcLeX0bBus",
    api_id="15316155",
    api_hash="c2340e29da60393bc3c96fa7c0870911"
)




@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
    text ="""
Hi bro
description"""  
     button=[[
       InlineKeyboardButton("𝕆𝕎ℕ𝔼ℝ", url="t.me/TEAM_KERALA"),
       InlineKeyboardButton("𝔻𝔼𝕍𝔼𝕃𝕆ℙ𝔼ℝ", url="t.me/TEAM_KERALA")
     ]]
     await message.reply_text(
         text=text,
         reply_markup=InlineKeyboardMarkup(button)
     )
       
Naruto.run()
