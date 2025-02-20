from aiogram import Dispatcher, Bot
from decouple import config

token = config("TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)

Admins = [1009418413, ]