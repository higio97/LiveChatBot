from bot.bot import Bot
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message, 
   InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
)
from bot import (
START_TEXT, START_IMG, URL_BUTTON) 

@Bot.on_message(filters.command("start"))
async def gstart(client: Client, message: Message):
     buttons = [
        [
            InlineKeyboardButton(
                "ππππ‘π‘ππ",
                url = URL_BUTTON)
        ]
    
    ]
     await message.reply_photo(
                photo= START_IMG, 
                caption = START_TEXT.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id, 
                language = message.from_user.language_code, 
                dc = message.from_user.dc_id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True
    )             
            


@Client.on_message(filters.command("help"))
async def help(client: Client, message: Message):
  await message.reply_text("""ππππ ππ»π³πΌ π¨π»πππΈ π¨ππ²πΏ:

β’ Silahkan pilih dan kirim konten yang ingin kalian Donate
β’ Tunggu sampai Admin Online, Chat kalian pasti akan dibalas

π¨π»πππΈ ππ±πΊπΆπ»:

β’/ban <alasan> - memblokir anak dajjal
β’/unban - membuka blokir anak haram

π‘πΌππ²:<code> Jangan melakukan spam Chat jika tidak ingin diban</code>
"""	
    )
