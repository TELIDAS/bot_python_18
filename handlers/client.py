from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot
from aiogram import types, Dispatcher
from keyboards import client_kb


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hello im your first bot",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply(f'Hello {message.from_user.username}! 😁\n'
                        f'I\'m your bot for filtering messages, so that\'s why be careful,'
                        f' i can ban you for curse words 😈\n'
                        f'Also i have some commands:\n'
                        f'1. /quiz1 this command for hilarious quiz '
                        f'questions, quiz has continue by clicking '
                        f'button *Следующая викторина*\n'
                        f'2. Also u can share location or info about u')


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Who invented Python"
    answers = [
        "Voldemort",
        "Harry Potter",
        "Linus Torvalds",
        "Guido Van Rossum"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        explanation="This is easy, not gonna explain\!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz1'])
