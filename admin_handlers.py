from aiogram import  types
from aiogram.types import ReplyKeyboardRemove

from main_variables import bot, dp, types

from config import ADMIN

from menus.admin.delete_menu import delete
from menus.users.main_menu import main_menu

@dp.message_handler(lambda message: message.text == '/start' and message.from_user.id in ADMIN and message.chat.type == 'private')
async def hello(message: types.Message):
    msg_text = """
Че надо-то?
    """
    await bot.send_message(message.chat.id, msg_text, reply_markup=main_menu)
    print(message)


#Узнаем id вашего чата
@dp.message_handler(lambda message: message.text == '/id')
async def return_chat_id(message: types.Message):
    await message.answer(f'Вот id вашего чата - {message.chat.id}')


# Удалить случайно вылезшое меню
@dp.message_handler(lambda message: message.text == '/clear' and message.from_user.id in ADMIN)
async def delete_menu(message: types.Message):
    await message.answer('А, ой', reply_markup=ReplyKeyboardRemove())