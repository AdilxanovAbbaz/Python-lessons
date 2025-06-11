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
    await message.answer(f"Вы выбрали {message.text}. Выберите день недели:", reply_markup=get_week_days_kb())

@dp.message_handler(Text(equals=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]))
async def handle_day_selection(message: types.Message):
    user_id = message.from_user.id
    selected_class = user_class.get(user_id)

    if not selected_class:
        await message.answer("Сначала выберите класс!", reply_markup=main_menu)
        return

    day = message.text
    schedule = schedule_data.get(selected_class, {}).get(day, ["Нет расписания"])
    formatted = "\n".join(schedule)
    await message.answer(f"Расписание на {day} для {selected_class}:\n\n{formatted}")


@dp.message_handler(Text(equals="Назад"))
async def handle_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню. Выберите класс:", reply_markup=main_menu)

