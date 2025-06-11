from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="7-А"),
            KeyboardButton(text="7-Б"),
            KeyboardButton(text="7-В"),
        ],
        [
            KeyboardButton(text="7-Г"),
            KeyboardButton(text="7-Д"),
            KeyboardButton(text="7-Е"),
        ],
        [
            KeyboardButton(text="7-Ж"),
        ],
    ],
    resize_keyboard=True
)
