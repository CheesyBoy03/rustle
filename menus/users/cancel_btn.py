# - * - coding: utf- 8 * -
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel = KeyboardButton('Отмена')\

cancel_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel)