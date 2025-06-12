from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from keyboards.default.main_menu import main_menu
from keyboards.default.week_days import get_week_days_kb
from data.schedule import schedule_data

user_class = {}

@dp.message_handler(Text(equals=["7-А", "7-Б", "7-В", "7-Г", "7-Д", "7-Е", "7-Ж"]))
async def handle_class_selection(message: types.Message):
    user_class[message.from_user.id] = message.text
    await message.answer("Выбери день недели:", reply_markup=get_week_days_kb())

@dp.message_handler(Text(equals=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]))
async def handle_day_selection(message: types.Message):
    class_selected = user_class.get(message.from_user.id)
    if not class_selected:
        await message.answer("Выберите свой класс")
        return

    schedule = schedule_data.get(class_selected, {}).get(message.text)
    if schedule:
        lessons = "\n".join([f"{i+1}. {lesson}" for i, lesson in enumerate(schedule)])
        await message.answer(f"Расписание на {message.text} ({class_selected}):\n{lessons}")
    else:
        await message.answer("Нет расписания на этот день.")

@dp.message_handler(Text(equals="Назад"))
async def go_back(message: types.Message):
    await message.answer("Выбери свой класс:", reply_markup=main_menu)
