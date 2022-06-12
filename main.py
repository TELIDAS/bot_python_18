from config import bot, dp
from aiogram.utils import executor
from handlers import client, callback_quiz, extra

client.register_handlers_client(dp)
callback_quiz.register_handlers_callback_quiz(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
