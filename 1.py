import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import Command
from aiogram.types import BotCommand, Message

TOKEN = "8610136354:AAE4te1Dgf1AcQFDaJ_-UD55YDWtCmmE2jk"
ADMIN_ID = 8527738147

bot = Bot(TOKEN)
dp = Dispatcher()

films = ["Titanik", "Inception", "Interstellar", "Forrest Gump", "The Matrix"]
genres = ["Komediya", "Drama", "Fantastika", "Triller", "Multfilm"]
actors = ["Leonardo DiCaprio", "Tom Hanks", "Keanu Reeves", "Will Smith"]


@dp.message()
async def to_admin(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.forward(ADMIN_ID)
    return UNHANDLED


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Salom! Men Kino botman 🎬")


@dp.message(Command("film"))
async def film(message: Message):
    await message.answer(random.choice(films))


@dp.message(Command("janr"))
async def janr(message: Message):
    await message.answer(random.choice(genres))


@dp.message(Command("aktyor"))
async def aktyor(message: Message):
    await message.answer(random.choice(actors))


@dp.message(Command("admin"))
async def admin(message: Message):
    await message.answer("Admin: @mashrabjon_09")


@dp.message(F.content_type.in_({"text", "photo", "video", "audio", "contact", "location"}))
async def content(message: Message):
    await message.answer("Siz yubordingiz: " + message.content_type)


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Boshlash"),
        BotCommand(command="film", description="Tasodifiy film"),
        BotCommand(command="janr", description="Tasodifiy janr"),
        BotCommand(command="aktyor", description="Tasodifiy aktyor"),
        BotCommand(command="admin", description="Admin"),
    ])
    await dp.start_polling(bot)


asyncio.run(main())