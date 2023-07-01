import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import *

API_TOKEN = '5888961083:AAHRBa7pS-cuhyG5V8ofdhilowtlqX1w090'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('''Assalomu alaykum! 

Botdan foydalanish uchun ushbu kanalga a'zo bo‘ling:
👉 t.me/audiokitoblar_uz

Используйте /off чтобы приостановить подписку.''',reply_markup=languvage_tili)
    await message.answer('''Хотите создать своего бота?
Вам сюда: @Manybot''',reply_markup=languvage_tili)


@dp.message_handler(text=["💿 O‘zbek adabiyoti 💿"])
async def send_welcome_uz(message: types.Message):
    await message.answer('🔘 Tanlang',
        reply_markup=boshlanish_tugmasi_uz)


@dp.message_handler(text="O‘tkan kunlar")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/933''',
        reply_markup=boshlanish_tugmasi_uz)


@dp.message_handler(text="Mehrobdan chayon")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/700''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Ufq")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/406''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Kecha va kunduz")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/275''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Avlodlar dovoni")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1014''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Yulduzli tunlar")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/890''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Navoiy")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1346''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Ulug‘bek xazinasi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/971''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Oltin zanglamas")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2193''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Jannati odamlar")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1422''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Otamdan qolgan dalalar")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/346''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Bu dunyoda o‘lib bo‘lmaydi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/264''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Yulduzlar mangu yonadi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1095''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Ot kishnagan oqshom")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/622''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Ikki eshik orasi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1680''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Dunyoning ishlari")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/306''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Daftar hoshiyasidagi bitiklar")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1903''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Bahor qaytmaydi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/14''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Tushda kechgan umrlar")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/183''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Nur borki soya bor")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1618''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Shum bola")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2359''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Bolalik")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1432''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="Bolalik")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1432''',
        reply_markup=boshlanish_tugmasi_uz)
    

@dp.message_handler(text="💿 Jahon adabiyoti 💿")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1432''',
        reply_markup=boshlanish_tugmasi)
        

@dp.message_handler(text="Choliqushi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1873''',
        reply_markup=boshlanish_tugmasi)
    

@dp.message_handler(text="Qon da'vosi")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1664''',
        reply_markup=boshlanish_tugmasi)
    

@dp.message_handler(text="Martin Iden")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2156''',
        reply_markup=boshlanish_tugmasi)
    

@dp.message_handler(text="Hikoyalar (Jek London)")
async def go_back(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/587''',
        reply_markup=boshlanish_tugmasi)
    

@dp.message_handler(text="🔘 Audio darsliklar 🔘")
async def go_back(message: types.Message):
    await message.answer('Audio darsliklar bu yerda: @audio_darsliklar',
        reply_markup=languvage_tili)
    

@dp.message_handler(text="🔘 Yangi audio kitoblar 🔘")
async def go_back(message: types.Message):
    await message.answer('''Yangi audio kitoblarni o‘tkazib yubormaslik uchun kanalimizga obuna bo‘lishni unutmang: 

t.me/audiokitoblar_uz''',
        reply_markup=languvage_tili)


@dp.message_handler(text="📨 Murojaat uchun 📨")
async def go_back(message: types.Message):
    await message.answer('''Murojaat uchun: 

@audiokitoblar_uzbot''',
        reply_markup=languvage_tili)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)