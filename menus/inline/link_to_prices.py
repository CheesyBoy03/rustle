from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

link = InlineKeyboardButton(text='Ознакомиться', url='https://t.me/rustleprice')

price_menu = InlineKeyboardMarkup().add(link)