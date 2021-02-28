from aiogram.dispatcher import FSMContext

from main_variables import bot, dp, types

from config import ADMIN, ADMIN_CHANNEL

from menus.users.main_menu import main_menu
from menus.users.cancel_btn import cancel_menu
from menus.inline.lint_to_prices import price_menu

from state import Ordering


# Встречаем нового пользователя нашего бота
@dp.message_handler(lambda message: message.text == '/start' and message.from_user.id not in ADMIN and message.chat.type == 'private')
async def hello(message: types.Message):
    msg_text = """
Здравствуйте, я бот веб-студии "Rustle Studio".
Че надо-то?
    """
    await bot.send_message(message.chat.id, msg_text, reply_markup=main_menu)
    print(message)


# Кнопка отмены оформления заказа, возвращает главное меню
@dp.message_handler(lambda message: message.text == 'Отмена' and message.chat.type == 'private')
async def cancel_of_ordering(message: types.Message, state=FSMContext):
    await state.finish()
    await message.answer('Отмена', reply_markup=main_menu)


# Возвращение списка услуг
@dp.message_handler(lambda message: message.text == 'Услуги' and message.chat.type == 'private')
async def answer_about_services(message: types.Message):
    await message.answer('Пока услуг нет, но скоро появятся, не переживайте')


# Отправляет ссылку на канал с прайс-листом
@dp.message_handler(lambda message: message.text == 'Цены' and message.chat.type == 'private')
async def link_to_prices(message: types.Message):
    await message.answer('Тут вы можете ознакомиться с нашим прайсом:', reply_markup=price_menu)


# Оформление заявки для заказа
@dp.message_handler(lambda message: message.text == 'Сделать заказ' and message.chat.type == 'private')
async def ordering(message: types.Message):
    await message.answer("""
Здравствуйте!

Для того, чтобы заказать дизайн - заполните форму 👇

1. Что хотите заказать?
2. В какие сроки нужно уложиться?

Вам ответят в течение 15 минут после заполнения заявки🐼
    """, reply_markup=cancel_menu)
    await Ordering.info_about_service.set()


@dp.message_handler(state=Ordering.info_about_service)
async def end_of_ordering(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text

        if message.text.lower() != 'отмена':
            await message.forward(ADMIN_CHANNEL)
            await message.answer('Спасибо, заказ принят. В скором времени с вами свяжутся', reply_markup=main_menu)
        else:
            await message.answer('Отмена заказа', reply_markup=main_menu)
        
        await state.finish()