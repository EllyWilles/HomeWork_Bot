from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.keyboards.keyboards import kb1, kb2
from less3.utils.randomfox import fox
from random import randint


router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет! {name}', reply_markup=kb1)


@router.message(Command("stop"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')


@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису')
    await message.answer_photo(photo=img_fox)


@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")


@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'I am a bot')
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри, что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')


