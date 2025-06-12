from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_week_days_kb():
    return ReplyKeyboardMarkup([
        [KeyboardButton("Понедельник"), KeyboardButton("Вторник")],
        [KeyboardButton("Среда"), KeyboardButton("Четверг")],
        [KeyboardButton("Пятница"), KeyboardButton("Суббота")],
        [KeyboardButton("Назад")]
    ], resize_keyboard=True)
