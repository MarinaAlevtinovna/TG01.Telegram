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

# @dp.message(Command('doc'))
# async def audio(message: Message):
#     doc = FSInputFile('111.pdf')
#     await bot.send_document(message.chat.id, doc)
#
# @dp.message(Command('video'))
# async def video(message: Message):
#     await bot.send_chat_action(message.chat.id, 'upload_video')
#     video = FSInputFile('video.mp4')
#     await bot.send_video(message.chat.id, video)
#
# @dp.message(Command('audio'))
# async def audio(message: Message):
#     audio = FSInputFile('sound.mp3')
#     await bot.send_audio(message.chat.id, audio)

# @dp.message(Command('voice'))
# async def voice(message: Message):
#     voice = FSInputFile('sample.ogg')
#     await message.answer_voice(voice)

# @dp.message(Command('training'))
# async def training(message: Message):
#     training_list = [
#         "Тренировка 1:\n 1. Скручивания: 3 подхода по 15 повторений\n 2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n 3. Планка: 3 подхода по 30 секунд",
#         "Тренировка 2:\n 1. Подъемы ног: 3 подхода по 15 повторений\n 2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n 3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
#         "Тренировка 3:\n 1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n 2. Горизонтальные ножницы: 3 подхода по 20 повторений\n 3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
#     ]
#     run_tr = random.choice(training_list)
#     await message.answer(f'Это ваша мини треня на сегодня: {run_tr}')
#     tts = gTTS(text=run_tr, lang='ru')
#     tts.save('train.ogg')
#     audio = FSInputFile('train.ogg')
#     await bot.send_voice(message.chat.id, audio)
#     os.remove('train.ogg')
#
# @dp.message(F.text == 'Что такое ИИ?')
# async def aitext(message: Message):
#     await message.answer('Искусственный интеллект (ИИ) — это область компьютерной науки, направленная на создание систем, которые могут выполнять задачи, требующие человеческого интеллекта, такие как обучение, анализ данных и принятие решений')
#
# @dp.message(F.photo)
# async def aiphoto(message: Message):
#     list = ['Ого! Какая фотка!', 'Непонятно что это такое', 'Не отправляй мне такое больше!']
#     rand_answ = random.choice(list)
#     await message.answer(rand_answ)
#     await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')
#
# @dp.message(Command('photo', prefix='&'))
# async def photo(message: Message):
#     list = ['https://i.pinimg.com/736x/fb/ca/59/fbca5904797c748e29b7f5601258baae.jpg', 'https://i.pinimg.com/736x/90/ec/77/90ec771d0fd97bbf0d18d9081cd1aafe.jpg', 'https://i.pinimg.com/736x/53/e6/f9/53e6f9d06b46b22321ed8f42ef365f51.jpg']
#     rand_photo = random.choice(list)
#     await message.answer_photo(photo=rand_photo, caption='Это круто!')
@dp.message(F.text == 'Тестовая кнопка 1')
async def test_button(message: Message):
    await message.answer('Обработка нажатия на reply кнопку')

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer('Новости подгружаются...', show_alert=True)
    await callback.message.edit_text('Вот свежие новости', reply_markup=await kb.test_keyboard())

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Дратути. {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)

# @dp.message()
# async def start1(message: Message):
#     await message.answer('Залупа!')

# @dp.message()
# async def start2(message: Message):
#     if message.text.lower() == 'тест':
#         await message.answer('тестируется')
#     await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())