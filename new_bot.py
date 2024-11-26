import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
import random
from gtts import gTTS
import os
from googletrans import Translator

import random

translator = Translator()

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.photo)
async def aiphoto(message: Message):
    list = ['Ого! Какая фотка!', 'Непонятно что это такое', 'Не отправляй мне такое больше!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Дратути. {message.from_user.first_name}')

@dp.message()
async def all_message_voice(message: Message):
    user_message = message.text
    translated_message = translator.translate(user_message, src='ru', dest='en').text
    tts = gTTS(text=translated_message, lang='en')
    await message.answer(translated_message)
    tts.save("voice_message.ogg")
    audio = FSInputFile('voice_message.ogg')
    await bot.send_voice(message.chat.id, audio)
    os.remove('voice_message.ogg')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())