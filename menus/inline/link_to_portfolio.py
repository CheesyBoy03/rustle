# - * - coding: utf- 8 * -
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# link = InlineKeyboardButton(text='Ознакомиться', url='https://t.me/rustleportfolio')

# portfolio_menu = InlineKeyboardMarkup().add(link)

web_design_btn = InlineKeyboardButton(
    text='Веб-дизайн', 
    url='https://t.me/rustleportfolio'
    )
layout_btn = InlineKeyboardButton(
    text='Верстка сайтов', 
    url='https://t.me/rustleportfolio'
    )
bots_btn = InlineKeyboardButton(
    text='Разработка ботов', 
    url='https://t.me/rustleportfolio'
    )
design_of_social_networks_btn = InlineKeyboardButton(
    text='Оформление соц. сетей', 
    url='https://t.me/rustleportfolio'
    )

portfolio_menu = InlineKeyboardMarkup().row(web_design_btn).row(layout_btn).row(bots_btn)