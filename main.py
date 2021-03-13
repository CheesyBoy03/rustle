from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from admin_handlers import *
from user_handlers import *


if __name__ == '__main__':
    executor.start_polling(dp)
