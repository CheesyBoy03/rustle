from aiogram.dispatcher.filters.state import State, StatesGroup


class Ordering(StatesGroup):
    info_about_service = State()
