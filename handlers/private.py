import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/520b104af857b36432b12.jpg",
        caption=f"""**тнιѕ ιѕ ℓσνєℓу вσт🥀 ρℓαу  ѕσηg ση тєℓєgяαм ν¢😅 тнιѕ вσт ωσякιηg ση ƒяєє ѕєяνєя😂  = [ᴶᵃᶜᵏ×͜×  ˢᵖᵃʳʳᵒʷ](t.me/Its_jack)
𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [ᴶᵃᶜᵏ×͜×  ˢᵖᵃʳʳᵒʷ](https://t.me/its_jack)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ Our BOTS❤️🎸](https://t.me/our_powerfull_bots)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨  Chat group 🎧](https://t.me/CHATTINGxGROUP)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [  😂😂😂  ](https://t.me/jackabout)
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [✨𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗡𝗼𝘄 🚩](https://telegra.ph/Commonds-02-03)
 = [ᴶᵃᶜᵏ×͜×  ˢᵖᵃʳʳᵒʷ](https://t.me/its_jack)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💗add me to your group😅💗", url=f"t.me/ansi_Ro_bot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fc98d41cfda83f4e31cd9.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://t.me/Friendschattinggrp")
                ]
            ]
        ),
    )
