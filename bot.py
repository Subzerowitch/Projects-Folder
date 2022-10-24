import time
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "5614571115:AAHlE7ZqP49lJMT5OLfff0AHgehxE85dNXw"
MESSAGE = "Have you programmed today {}?"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hello {user_full_name}.")

    for i in range(7):
        time.sleep(60*60*24)
        await bot.send_message(user_id, MESSAGE.format(user_name))

if __name__ == '__main__':
    executor.start_polling(dp)
