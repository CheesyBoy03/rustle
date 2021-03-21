# - * - coding: utf- 8 * -
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

link = InlineKeyboardButton('Ознакомиться', url="https://t.me/rustleotziv")

reviews_menu = InlineKeyboardMarkup().add(link)