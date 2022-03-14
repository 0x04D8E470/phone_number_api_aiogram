from cgitb import text
from aiogram import types
from aiogram.dispatcher import filters
from config import UnkownMessage
from app import dp

@dp.message_handler()
async def unkown_msg(message: types.Message):
    await message.answer(UnkownMessage)