import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6448848530:AAHfHdk5pB28WLnq4grHzdYTVEtJ6tPQsa4")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)
async def main():
    await dp.start_polling(bot)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Этот бот может посоветовать вам фильмы")

@dp.message(Command("комедия"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--comedy/?b=films&utm_referrer=yandex.ru")

@dp.message(Command("боевик"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--action/")

@dp.message(Command("детектив"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--mystery/?b=top")

@dp.message(Command("драма"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--drama/?b=films")

@dp.message(Command("мелодрама"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--romance/?b=top")

@dp.message(Command("мистика"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kp.ru/afisha/msk/obzory/kino/luchshie-misticheskie-filmy/")

@dp.message(Command("приключения"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--adventure/")

@dp.message(Command("триллер"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--thriller/?b=films&b=top")

@dp.message(Command("ужастик"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--horror/?b=films")

@dp.message(Command("фантастика"))
async def cmd_test1(message: types.Message):
    await message.reply("https://www.kinopoisk.ru/lists/movies/genre--sci-fi/?b=films")

# Где-то в другом месте, например, в функции main():
@dp.message(Command("жанр"))
async def cmd_жанр(message: types.Message):
    kb = [
        [types.KeyboardButton(text="/комедия")],
        [types.KeyboardButton(text="/боевик")],
        [types.KeyboardButton(text="/детектив")],
        [types.KeyboardButton(text="/драма")],
        [types.KeyboardButton(text="/мелодрама")],
        [types.KeyboardButton(text="/мистика")],
        [types.KeyboardButton(text="/приключения")],
        [types.KeyboardButton(text="/триллер")],
        [types.KeyboardButton(text="/ужастик")],
        [types.KeyboardButton(text="/фантастика")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какой жанр вы выберите", reply_markup=keyboard)
if __name__ == "__main__":
    asyncio.run(main())
