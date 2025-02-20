from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot

async def quiz(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Далее', callback_data='button_1')
    keyboard.add(button)
    question = 'Какое время года?'
    answer = ['Лето', "зима", 'осень', "весна"]

    with open('media/test.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='🍂',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Далее', callback_data='button_2')
    keyboard.add(button)

    question = 'Dota2 or CS.GO'
    answer = ['Dota2', 'CS.GO', 'Valve']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    question = 'Java or JavaScript'
    answer = ['Java', 'JavaScript', 'Python']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        explanation='🐍',
        type='quiz',
        correct_option_id=2,
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')
