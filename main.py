from decouple import config

from config import bot, dp, URL
from aiogram.utils import executor
from handlers import client, callback_quiz, extra, admin, notification, inline
from database import bot_db, psql_db
import asyncio

""""
Polling:
heroku ps:scale worker=1
heroku ps:scale worker=0

Webhook:
heroku ps:scale web=1
heroku ps:scale web=0

heroku logs --tail --app pythongeekbot18
"""


async def on_startup(_):
    await bot.set_webhook(URL)
    bot_db.sql_create()
    psql_db.psql_create()
    print("Bot is online")
    asyncio.create_task(notification.scheduler())


async def on_shutdown(dp):
    await bot.delete_webhook()


client.register_handlers_client(dp)
admin.register_handler_admin(dp)
callback_quiz.register_handlers_callback_quiz(dp)
inline.register_handlers_inline(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    # executor.start_polling(dp,
    #                        skip_updates=True,
    #                        on_startup=on_startup
    #                        )
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(config("PORT", default=5000))
    )
