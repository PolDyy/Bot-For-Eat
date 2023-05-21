from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


