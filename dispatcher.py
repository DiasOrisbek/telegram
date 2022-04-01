#DISPETCHER TELEGRAMBOT

from main import bot, dp

from aiogram.types import Message
from config import my_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text = "My name is Dias!")

@dp.message_handler()
async def echo(message:Message):
    text = f"Salem,sen tochno '{message.text}' degendi zhazgyn keldi ma?"
    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler()
async def echo(message:Message):
    text = "Hello Bro!"
    await bot.send_message(chat_id=message.from_user.id, text=text)

    