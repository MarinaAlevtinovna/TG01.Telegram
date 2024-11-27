import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import random
from gtts import gTTS
import os

import random
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.callback_query(F.data == 'hello')
async def hello(callback: CallbackQuery):
    await callback.answer('...')
    await callback.message.answer(f'Дратути, {callback.from_user.first_name}')

@dp.callback_query(F.data == 'bye')
async def bye(callback: CallbackQuery):
    await callback.answer('...')
    await callback.message.answer(f'Ну покеда, {callback.from_user.first_name}')

@dp.callback_query(F.data == 'see_more')
async def see_more(callback: CallbackQuery):
   await callback.answer("...")
   await callback.message.edit_text('Опции', reply_markup=kb.see_more_o)

@dp.callback_query(F.data == 'option1')
async def option1(callback: CallbackQuery):
   await callback.answer("...")
   await callback.message.answer('Опция1')

@dp.callback_query(F.data == 'option2')
async def option2(callback: CallbackQuery):
   await callback.answer("...")
   await callback.message.answer('Опция2')


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Показать больше', reply_markup=kb.see_more)


@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Чем займешься?', reply_markup= await kb.test_keyboard())
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Бот на связи!', reply_markup=kb.inline_keyboard_test)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())