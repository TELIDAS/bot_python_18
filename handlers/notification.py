import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


# 1150258083
async def standup():
    ADMIN_ID = 1150258083
    await bot.send_message(
        chat_id=ADMIN_ID,
        text="Не забудь написать standup"
    )


async def scheduler():
    aioschedule.every().tuesday.at("20:40").do(standup)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)
