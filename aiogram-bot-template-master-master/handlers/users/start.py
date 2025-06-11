from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from keyboards.default.main_menu import main_menu

@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(reply_markup=main_menu)
