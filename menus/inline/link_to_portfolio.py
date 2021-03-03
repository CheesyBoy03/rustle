from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

link = InlineKeyboardButton(text='Ознакомиться', url='https://t.me/rustleportfolio')

portfolio_menu = InlineKeyboardMarkup().add(link)