import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('Искусственный интеллект (ИИ) — это область компьютерной науки, направленная на создание систем, которые могут выполнять задачи, требующие человеческого интеллекта, такие как обучение, анализ данных и принятие решений')

@dp.message(F.photo)
async def aiphoto(message: Message):
    list = ['Ого! Какая фотка!', 'Непонятно что это такое', 'Не отправляй мне такое больше!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://i.pinimg.com/736x/fb/ca/59/fbca5904797c748e29b7f5601258baae.jpg', 'https://i.pinimg.com/736x/90/ec/77/90ec771d0fd97bbf0d18d9081cd1aafe.jpg', 'https://i.pinimg.com/736x/53/e6/f9/53e6f9d06b46b22321ed8f42ef365f51.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это круто!')
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')
@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Дратути. Я ботик!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())