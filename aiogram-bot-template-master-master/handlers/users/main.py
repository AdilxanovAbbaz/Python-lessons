from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink
@dp.message_handler(commands="info")
async def info(message: types.Message):
    text = f"Assalamu aleykum, {message.from_user.full_name}!\n"
    text +="Bul" + hbold("qalin text. \n")
    text += "Bul "+ hitalic(" qiysiq text.\n")
    text += "Bul "+ hunderline(" astinda sizig'i bar text. \n")
    text += "Bul "+ hstrikethrough(" oshirilgen text.\n")
    text += "Bul "+ hlink('Formatlawdin linki \n', "https://core.telegram.org/bots/api#formatting-options")
    text += "Bul "+ hcode("Hello World!")
    await message.answer(text)