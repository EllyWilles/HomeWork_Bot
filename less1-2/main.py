import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from keyboards import kb1, kb2
from randomfox import fox
from random import randint

API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет! {name}', reply_markup=kb1)


@dp.message(Command("stop"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')


@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису')
    await message.answer_photo(photo=img_fox)


@dp.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")


@dp.message(F.text)
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



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())