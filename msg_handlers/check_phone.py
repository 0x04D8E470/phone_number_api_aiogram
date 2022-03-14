from aiogram import types
from aiogram.dispatcher import filters
from app import dp
from config import PHONE_REGEXP
from phone_api.check_number import check_number
import re

@dp.message_handler(filters.Regexp(PHONE_REGEXP))
async def check_phone(message: types.Message):
    await message.answer(check_number(message.text))