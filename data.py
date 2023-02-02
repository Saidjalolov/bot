# kerakli modullarni chaqirib olamiz
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging
from tugmalar import natija,natija2


# Logging qismi
logging.basicConfig(level=logging.INFO)

# Botni ulash qismi
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {ism}. Botimizga xush kelibsiz.",reply_markup=natija)

# @dp.message_handler()
# async def buttons(message: types.Message):
#     if message.text == "Joylashuv":
#         await message.answer_location(41.334896756804774, 69.21547319114438)
#         await message.answer("<b>Bizning manzil</b>: Beruniy ko'chasi 35A.\n<b>Mo'ljal</b>: Bursa restorani yonida", parse_mode="HTML")
#     elif message.text == "Telefon raqam":
#         await message.answer_contact(phone_number="+998931234567",first_name="Mars",last_name="IT School")

@dp.callback_query_handler(lambda b: b.data == "uz")
async def uzbek(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Siz o'zbek tilini tanladingiz", reply_markup=natija2)

@dp.message_handler(text="Ma'lumot")
async def malumot(message: types.Message):
     await message.answer_photo("https://uznayvse.ru/images/catalog/2022/2/cristiano-ronaldo_56.jpg",caption="Cristiano Ronaldo dos Santos Aveiro")
     await message.answer("Salom")

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
