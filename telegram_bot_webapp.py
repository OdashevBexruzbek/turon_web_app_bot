# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command
# from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# # Bot token
# BOT_TOKEN = "8052905140:AAETPMISHM8ViW77p3svdlwrMRx5kjgUGZc"

# # Web App URL (Serveringiz URL)
# WEB_APP_URL = "https://turonapp.netlify.app/"
# # Development uchun: WEB_APP_URL = "http://localhost:8000/turon_cafe_app_with_backend.html"

# # Logging
# logging.basicConfig(level=logging.INFO)

# # Bot va Dispatcher
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def cmd_start(message: Message):
#     """Start buyrug'i - Web App ni ochish"""
    
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(
#             text="🍽️ Buyurtma berish",
#             web_app=WebAppInfo(url=WEB_APP_URL)
#         )],
#         [InlineKeyboardButton(
#             text="📞 Bog'lanish",
#             callback_data="contact"
#         )]
#     ])
    
#     await message.answer(
#         "🌟 Turon kafesiga xush kelibsiz!\n\n"
#         "📱 Buyurtma berish uchun quyidagi tugmani bosing.\n"
#         "🚀 Tez, qulay va oson!\n\n"
#         "☎️ Aloqa: +998 90 123 45 67\n"
#         "📍 Manzil: Toshkent shahar, Amir Temur ko'chasi",
#         reply_markup=keyboard
#     )

# @dp.callback_query(F.data == "contact")
# async def show_contact(callback):
#     """Kontakt ma'lumotlarini ko'rsatish"""
#     await callback.message.answer(
#         "📞 BOG'LANISH:\n\n"
#         "☎️ Telefon: +998 90 123 45 67\n"
#         "📱 Telegram: @turon_cafe\n"
#         "📧 Email: info@turoncafe.uz\n"
#         "📍 Manzil: Toshkent shahar, Amir Temur ko'chasi, 123-uy\n\n"
#         "🕐 Ish vaqti: 10:00 - 23:00 (har kuni)"
#     )
#     await callback.answer()

# @dp.message()
# async def echo_message(message: Message):
#     """Boshqa xabarlar"""
#     await message.answer(
#         "Buyurtma berish uchun /start buyrug'ini bosing! 🍽️"
#     )

# async def main():
#     """Bot ishga tushirish"""
#     print("🤖 Bot ishga tushdi!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Bot token - backend_server.py dan
BOT_TOKEN = "8052905140:AAETPMISHM8ViW77p3svdlwrMRx5kjgUGZc"

# Web App URL - sizning Netlify URL (o'zgartirib kiriting!)
# WEB_APP_URL = "https://your-netlify-site.netlify.app"  # BU JOYNI O'ZGARTIRING!

# # Logging
# logging.basicConfig(level=logging.INFO)

# # Bot va Dispatcher
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def cmd_start(message: Message):
#     """Start buyrug'i - Web App ni ochish"""
    
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(
#             text="🍽️ Buyurtma berish",
#             web_app=WebAppInfo(url=WEB_APP_URL)
#         )],
#         [InlineKeyboardButton(
#             text="📞 Bog'lanish",
#             callback_data="contact"
#         )]
#     ])
    
#     await message.answer(
#         "🌟 Turon kafesiga xush kelibsiz!\n\n"
#         "📱 Buyurtma berish uchun quyidagi tugmani bosing.\n"
#         "🚀 Tez, qulay va oson!\n\n"
#         "☎️ Aloqa: +998 90 123 45 67\n"
#         "📍 Manzil: Toshkent shahar, Amir Temur ko'chasi",
#         reply_markup=keyboard
#     )

# @dp.callback_query(F.data == "contact")
# async def show_contact(callback):
#     """Kontakt ma'lumotlarini ko'rsatish"""
#     await callback.message.answer(
#         "📞 BOG'LANISH:\n\n"
#         "☎️ Telefon: +998 90 123 45 67\n"
#         "📱 Telegram: @turon_cafe\n"
#         "📧 Email: info@turoncafe.uz\n"
#         "📍 Manzil: Toshkent shahar, Amir Temur ko'chasi, 123-uy\n\n"
#         "🕐 Ish vaqti: 10:00 - 23:00 (har kuni)"
#     )
#     await callback.answer()

# @dp.message()
# async def echo_message(message: Message):
#     """Boshqa xabarlar"""
#     await message.answer(
#         "Buyurtma berish uchun /start buyrug'ini bosing! 🍽️"
#     )

# async def main():
#     """Bot ishga tushirish"""
#     print("🤖 Bot ishga tushdi!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot token va URL
BOT_TOKEN = "8052905140:AAETPMISHM8ViW77p3svdlwrMRx5kjgUGZc"
WEB_APP_URL = "https://turon-web-app-bot.vercel.app"
# Development uchun:
WEB_APP_URL = "http://localhost:8000/turon_cafe_app_with_backend.html"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Start buyrug'i - Buttonlar ko'rsatish"""
    
    # Inline keyboard yaratish
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🍽️ Buyurtma berish",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )],
        [InlineKeyboardButton(
            text="📞 Bog'lanish",
            callback_data="contact"
        )],
        [InlineKeyboardButton(
            text="ℹ️ Ma'lumot",
            callback_data="info"
        )]
    ])
    
    await message.answer(
        "🌟 <b>Turon kafesiga xush kelibsiz!</b>\n\n"
        "📱 Buyurtma berish uchun quyidagi tugmani bosing.\n"
        "🚀 Tez, qulay va oson!\n\n"
        "☎️ Aloqa: +998 90 123 45 67\n"
        "📍 Manzil: Toshkent shahar",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "contact")
async def show_contact(callback):
    """Kontakt ma'lumotlari"""
    await callback.message.answer(
        "📞 <b>BOG'LANISH:</b>\n\n"
        "☎️ Telefon: +998 90 123 45 67\n"
        "📱 Telegram: @turon_cafe\n"
        "📧 Email: info@turoncafe.uz\n"
        "📍 Manzil: Toshkent shahar\n\n"
        "🕐 Ish vaqti: 10:00 - 23:00 (har kuni)",
        parse_mode="HTML"
    )
    await callback.answer()

@dp.callback_query(F.data == "info")
async def show_info(callback):
    """Ma'lumot"""
    await callback.message.answer(
        "ℹ️ <b>TURON KAFE</b>\n\n"
        "🍕 Eng mazali taomlar\n"
        "🚚 Tez yetkazib berish\n"
        "💰 Qulay narxlar\n"
        "⭐ Yuqori sifat\n\n"
        "Bizni tanlang, sifatni his eting!",
        parse_mode="HTML"
    )
    await callback.answer()

async def main():
    print("🤖 Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())