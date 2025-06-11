from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("7-А"), KeyboardButton("7-Б"), KeyboardButton("7-В")],
        [KeyboardButton("7-Г"), KeyboardButton("7-Д"), KeyboardButton("7-Е")],
        [KeyboardButton("7-Ж")]
    ],
    resize_keyboard=True
)
