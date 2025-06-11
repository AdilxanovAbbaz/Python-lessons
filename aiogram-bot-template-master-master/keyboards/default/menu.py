from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu= ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="KI"),
        KeyboardButton(text="DI"),
        KeyboardButton(text="JI"),
    ]
    ],
    resize_keyboard=True
)