from aiogram import Bot, Dispatcher
from decouple import config
# pip install python-decouple

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
