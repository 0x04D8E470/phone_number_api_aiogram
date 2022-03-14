from cgitb import text
from aiogram import Bot, Dispatcher, executor
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

if __name__ == "__main__":
    from msg_handlers import dp
    executor.start_polling(dp, skip_updates=True)