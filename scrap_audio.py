import os

import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get("TELEGRAM_BOT_API")

bot = telebot.TeleBot(API_TOKEN)

# chat_id = os.environ.get("CHAT_ID")

bot.infinity_polling()
