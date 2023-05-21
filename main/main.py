from aiogram import executor
from config import dp

import custom_handlers.handlers

executor.start_polling(dp)
