from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot
from aiogram import types, Dispatcher

from database import bot_db, psql_db
from keyboards import client_kb
from parser import scrapy_doramy


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hello im your first bot",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'Hello {message.from_user.username}! \n'
                           f'I\'m your bot for filtering messages, so that\'s why be careful,'
                           f' i can ban you for curse words \n'
                           f'Also i have some commands:\n'
                           f'1. /quiz1 this command for hilarious quiz '
                           f'questions, quiz has continue by clicking '
                           f'button *Следующая викторина*\n')
                           # f'2. Also u can share location or info about u\n'
                           # f'3. /shows U can watch collection of TV-Shows\n'
                           # f'4. /parser parse and see from doramy site\n'
                           # f'5. /doramy u can see all parsed shows from doramy site\n',
                           # f'6. /register u can register your data to bot')


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


async def get_all_tvshows(message: types.Message):
    await bot_db.sql_select(message)


async def get_all_doramy(message: types.Message):
    await bot_db.sql_select_doramy(message)


async def parser_doramy(message: types.Message):
    data = scrapy_doramy.scrapy_script()
    for shows in data:
        await bot_db.sql_insert_doramy(shows)
        await bot.send_message(message.chat.id,
                               shows)


async def registration(message: types.Message):
    id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    psql_db.cursor.execute(
        "INSERT INTO users (id, username, fullname) VALUES (%s, %s, %s)", (id, username, full_name), )
    psql_db.db.commit()
    await message.reply("Registration successful")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz1'])
    dp.register_message_handler(get_all_tvshows, commands=['shows'])
    dp.register_message_handler(get_all_doramy, commands=['doramy'])
    dp.register_message_handler(parser_doramy, commands=['parser'])
    dp.register_message_handler(registration, commands=['register'])
