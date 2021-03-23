from aiogram import  types
from aiogram.types import ReplyKeyboardRemove

import logging
import datetime

from main_variables import bot, dp, types

from config import ADMIN

from menus.users.main_menu import main_menu

import tg_analytic


#Узнаем id вашего чата
@dp.message_handler(lambda message: message.text == '/id')
async def return_chat_id(message: types.Message):
    await message.answer(f'Вот id вашего чата - {message.chat.id}')


# Удалить случайно вылезшое меню
@dp.message_handler(lambda message: message.text == '/clear' and message.from_user.id in ADMIN)
async def delete_menu(message: types.Message):
    await message.answer('А, ой', reply_markup=ReplyKeyboardRemove())


# Получаем статистику о пользователях или(и) о использованных командах
@dp.message_handler(lambda message: message.text[:10].lower() == 'статистика' and message.from_user.id in ADMIN)
async def test(message: types.Message):
    st = message.text.split(' ')

    try:
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st,message.chat.id)
            with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
                await bot.send_document(message.chat.id,file)
            tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st,message.chat.id)
            await bot.send_message(message.chat.id, messages) 
    except Exception:
        with open('logging.txt', 'a') as file_logging:
            file_logging.write(f'{datetime.datetime.now()}: {message}')