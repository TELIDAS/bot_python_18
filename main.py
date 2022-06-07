from aiogram import types
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp
from aiogram.utils import executor


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.reply("Hello World")
    await message.reply("Hello World x2")
    await bot.send_message(message.chat.id,
                           "Hello im your first bot")


@dp.message_handler(commands=['quiz1'])
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Who invented Linux"
    answers = [
        "Chepolinko",
        "Mario",
        "Linus Torvalds",
        "James bond"
    ]
    print(call.message.chat.id)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation="This is easy, not gonna explain\!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
