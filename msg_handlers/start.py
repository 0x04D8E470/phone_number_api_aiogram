from aiogram import types
from app import dp

from config import start_msg


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(start_msg)

# Обязательно надо добавить from msg_handlers.start (вместо start должно быть название файла, где хандлер)
# import dp в __init__.py, чтобы зарегать хандлер