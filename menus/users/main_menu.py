from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

make_an_order = KeyboardButton('Сделать заказ')

portfolio = KeyboardButton('Портфолио')
reviews = KeyboardButton('Отзывы')

services = KeyboardButton('Услуги')
price = KeyboardButton('Цены')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(make_an_order).row(portfolio, reviews).row(services, price)