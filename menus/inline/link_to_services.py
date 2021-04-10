# - * - coding: utf- 8 * -
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

link = InlineKeyboardButton('👉🏻 Ознакомиться', url='https://t.me/rustleuslugi')

services_menu = InlineKeyboardMarkup().add(link)