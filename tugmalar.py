from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup



uz =   InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data="uz")
ru =   InlineKeyboardButton(text="Rus tili🇷🇺",callback_data="ru")
us =   InlineKeyboardButton(text="Ingliz tili🇺🇸",callback_data="us")




info = KeyboardButton(text="Ma'lumot")
xodimlar =KeyboardButton(text="Xodmlar xaqida malumot")
yordam =KeyboardButton(text="Nima yordamim tegshi mumkin")
savollar =KeyboardButton(text="Savollar")
til =KeyboardButton(text="tilni tanlang")



contact = KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
location = KeyboardButton(text="Lokatsiya yuborish", request_location=True)
kurslar = KeyboardButton(text="Kurslar")
joylashuv = KeyboardButton(text="Joylashuv")
telefon_raqam = KeyboardButton(text="Telefon raqam")



natija = InlineKeyboardMarkup(row_width=3).add(uz,ru,us)
natija2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(info).add(xodimlar).add(yordam).add(savollar,til)