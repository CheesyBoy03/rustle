from aiogram.dispatcher import FSMContext

from main_variables import bot, dp, types

from config import ADMIN, ADMIN_CHANNEL

from menus.users.main_menu import main_menu
from menus.users.cancel_btn import cancel_menu
from menus.inline.link_to_prices import price_menu
from menus.inline.link_to_portfolio import portfolio_menu
from menus.inline.link_to_services import services_menu
from menus.inline.link_to_reviews import reviews_menu

from state import Ordering

import tg_analytic


# Встречаем нового пользователя нашего бота
@dp.message_handler(lambda message: message.text == '/start' and message.from_user.id not in ADMIN and message.chat.type == 'private')
async def hello(message: types.Message):
    tg_analytic.statistics(message.chat.id, message.text)
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


# Отправляет ссылку на канал с прайс-листом
@dp.message_handler(lambda message: message.text == 'Отзывы' and message.chat.type == 'private')
async def link_to_prices(message: types.Message):
    tg_analytic.statistics(message.chat.id, message.text)
    await message.answer('Только самые правдивые отзывы: ', reply_markup=reviews_menu)


# Отправляет ссылку на канал с прайс-листом
@dp.message_handler(lambda message: message.text == 'Цены' and message.chat.type == 'private')
async def link_to_prices(message: types.Message):
    tg_analytic.statistics(message.chat.id, message.text)
    await message.answer('Актуальные цены на сегодняшний день:', reply_markup=price_menu)


# Отправляет ссылку на канал с портфолио
@dp.message_handler(lambda message: message.text == 'Портфолио' and message.chat.type == 'private')
async def link_to_portfolio(message: types.Message):
    tg_analytic.statistics(message.chat.id, message.text)
    await message.answer('Что вас интересует?', reply_markup=portfolio_menu)


# Отправляет ссылку на канал со списком предоставляемых услуг
@dp.message_handler(lambda message: message.text == 'Услуги' and message.chat.type == 'private')
async def link_to_services(message: types.Message):
    tg_analytic.statistics(message.chat.id, message.text)
    await message.answer('Тут вы можете ознакомиться с нашими услугами:', reply_markup=services_menu)


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