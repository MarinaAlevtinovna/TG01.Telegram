from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Тестовая кнопка 1')],
#     [KeyboardButton(text='Тестовая кнопка 2')],
#     [KeyboardButton(text='Тестовая кнопка 3')]
# ], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Привет!', callback_data='hello')],
    [InlineKeyboardButton(text='Пока', callback_data='bye')],
])

# inline_keyboard_test2 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Новости', callback_data='news')],
#     [InlineKeyboardButton(text='Музыка', callback_data='music')],
#     [InlineKeyboardButton(text='Видео', callback_data='video')],
# ])

test = [
    {'text': 'Новости', 'url': 'https://smotrim.ru'},
    {'text': 'Музыка', 'url': 'https://yabs.yandex.ru'},
    {'text': 'Видео', 'url': 'https://rutube.ru/'},
]
# async def test_keyboard():
#      keyboard = ReplyKeyboardBuilder()
#      for key in test:
#          keyboard.add(KeyboardButton(text=key))
#      return keyboard.adjust(2).as_markup()

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for item in test:
        keyboard.add(InlineKeyboardButton(text=item['text'], url=item['url']))
    return keyboard.adjust(3).as_markup()

see_more = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data='see_more')],
    ])

see_more_o = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Опция1', callback_data='option1')],
    [InlineKeyboardButton(text='Опция2', callback_data='option2')],
])
