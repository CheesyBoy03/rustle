from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN, ADMIN

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())