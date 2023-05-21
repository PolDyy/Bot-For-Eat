from aiogram import types
from aiogram.types.message import ContentTypes, ContentType
from config import dp
from buttons.buttons import CustomMarkups
from custom_handlers.text_messages import get_start_message, get_answer_for_text


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = CustomMarkups.get_start_markup()
    answer = get_start_message(message)
    await message.answer(answer, reply_markup=markup)


@dp.message_handler(content_types=ContentTypes.TEXT)
async def text_message(message: types.Message):
    markup = CustomMarkups.get_start_markup()
    answer = get_answer_for_text(message)
    await message.answer(answer, reply_markup=markup)
