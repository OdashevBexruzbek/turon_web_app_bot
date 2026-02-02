import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Web App URL (Serveringiz URL)
WEB_APP_URL = "https://yourserver.com/turon_cafe_app_with_backend.html"
# Development uchun: WEB_APP_URL = "http://localhost:8000/turon_cafe_app_with_backend.html"

# Logging
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Start buyrug'i - Web App ni ochish"""
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🍽️ Buyurtma berish",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )],
        [InlineKeyboardButton(
            text="📞 Bog'lanish",
            callback_data="contact"
        )]
    ])
    
    await message.answer(
        "🌟 Turon kafesiga xush kelibsiz!\n\n"
        "📱 Buyurtma berish uchun quyidagi tugmani bosing.\n"
        "🚀 Tez, qulay va oson!\n\n"
        "☎️ Aloqa: +998 90 123 45 67\n"
        "📍 Manzil: Toshkent shahar, Amir Temur ko'chasi",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "contact")
async def show_contact(callback):
    """Kontakt ma'lumotlarini ko'rsatish"""
    await callback.message.answer(
        "📞 BOG'LANISH:\n\n"
        "☎️ Telefon: +998 90 123 45 67\n"
        "📱 Telegram: @turon_cafe\n"
        "📧 Email: info@turoncafe.uz\n"
        "📍 Manzil: Toshkent shahar, Amir Temur ko'chasi, 123-uy\n\n"
        "🕐 Ish vaqti: 10:00 - 23:00 (har kuni)"
    )
    await callback.answer()

@dp.message()
async def echo_message(message: Message):
    """Boshqa xabarlar"""
    await message.answer(
        "Buyurtma berish uchun /start buyrug'ini bosing! 🍽️"
    )

async def main():
    """Bot ishga tushirish"""
    print("🤖 Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
