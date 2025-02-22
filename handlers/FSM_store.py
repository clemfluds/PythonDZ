from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_store(StatesGroup):
    model_name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await FSM_store.model_name.set()
    await message.answer('Название модели: ')


async def load_model_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model_name'] = message.text

    await FSM_store.next()
    await message.answer('Размер:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_store.next()
    await message.answer('Категория: ')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text


    await FSM_store.next()
    await message.answer('Стоимость:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text


    await FSM_store.next()
    await message.answer('Фото товара: ')



async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSM_store.next()
    await message.answer('Верные ли данные')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Модель - {data["model_name"]}\n'
                                       f'Размер - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Стоимость - {data["price"]}\n'
                                       f'Фото - {data["photo"]}\n')

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            # Запись в базу
            await message.answer('Ваши данные в базе')
        await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['Store'])
    dp.register_message_handler(load_model_name, state=FSM_store.model_name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_store.submit)