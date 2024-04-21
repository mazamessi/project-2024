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
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    await message.answer("My name is Ivan")
    await message.answer("I can help you")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

# Где-то в другом месте, например, в функции main():
dp.message.register(cmd_test2, Command("test2"))

if __name__ == "__main__":
    asyncio.run(main())
