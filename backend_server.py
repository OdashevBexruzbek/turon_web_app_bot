from aiogram import Bot
from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
import logging
from datetime import datetime

# Configuration
BOT_TOKEN = "8052905140:AAETPMISHM8ViW77p3svdlwrMRx5kjgUGZc"
ADMIN_ID = 8132914660  # Admin Telegram ID

# Flask app
app = Flask(__name__)
CORS(app)  # CORS ni yoqish

# Bot
bot = Bot(token=BOT_TOKEN)

# Logging
logging.basicConfig(level=logging.INFO)

# Database (oddiy holat uchun dict, haqiqiy loyiha uchun PostgreSQL/MongoDB ishlatish kerak)
users_db = {}
orders_db = []

@app.route('/api/register', methods=['POST'])

def register_user():
    """Foydalanuvchi ro'yxatdan o'tishi"""
    try:
        data = request.json
        user_id = data.get('telegram_id')
        
        users_db[user_id] = {
            'first_name': data.get('firstName'),
            'last_name': data.get('lastName'),
            'phone': data.get('phone'),
            'address': data.get('address'),
            'registered_at': datetime.now().isoformat()
        }
        
        # Adminga xabar yuborish
        message = (
            "🆕 YANGI FOYDALANUVCHI RO'YXATDAN O'TDI!\n\n"
            f"👤 Ism: {data.get('firstName')} {data.get('lastName')}\n"
            f"📱 Telefon: {data.get('phone')}\n"
            f"📍 Manzil: {data.get('address')}\n"
            f"🆔 User ID: {user_id}\n"
            f"📅 Vaqt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        asyncio.run(send_telegram_message(ADMIN_ID, message))
        
        return jsonify({
            'status': 'success',
            'message': 'Ro\'yxatdan muvaffaqiyatli o\'tdingiz!'
        })
    
    except Exception as e:
        logging.error(f"Registration error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/order', methods=['POST'])
def create_order():
    """Buyurtma yaratish"""
    try:
        data = request.json
        user_id = data.get('telegram_id')
        
        # Buyurtmani saqlash
        order = {
            'id': len(orders_db) + 1,
            'user_id': user_id,
            'product': data.get('product'),
            'user_info': users_db.get(user_id, {}),
            'created_at': datetime.now().isoformat()
        }
        orders_db.append(order)
        
        # Adminga xabar
        product = data.get('product', {})
        user = users_db.get(user_id, {})
        
        message = (
            "🔔 YANGI BUYURTMA!\n\n"
            f"📦 Mahsulot: {product.get('name')}\n"
            f"💰 Narxi: {product.get('price'):,} so'm\n"
            f"📝 Tavsif: {product.get('desc')}\n\n"
            f"👤 BUYURTMACHI:\n"
            f"Ism: {user.get('first_name')} {user.get('last_name')}\n"
            f"📱 Telefon: {user.get('phone')}\n"
            f"📍 Manzil: {user.get('address')}\n"
            f"🆔 User ID: {user_id}\n"
            f"🔢 Buyurtma ID: #{order['id']}\n"
            f"📅 Vaqt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        asyncio.run(send_telegram_message(ADMIN_ID, message))
        
        return jsonify({
            'status': 'success',
            'order_id': order['id'],
            'message': 'Buyurtma qabul qilindi!'
        })
    
    except Exception as e:
        logging.error(f"Order error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    """Barcha buyurtmalar"""
    return jsonify({
        'status': 'success',
        'orders': orders_db
    })

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """Foydalanuvchi ma'lumotlari"""
    user = users_db.get(user_id)
    if user:
        return jsonify({
            'status': 'success',
            'user': user
        })
    return jsonify({
        'status': 'error',
        'message': 'Foydalanuvchi topilmadi'
    }), 404

async def send_telegram_message(chat_id, text):
    """Telegram orqali xabar yuborish"""
    try:
        await bot.send_message(chat_id=chat_id, text=text)
        logging.info(f"Message sent to {chat_id}")
    except Exception as e:
        logging.error(f"Telegram send error: {e}")

@app.route('/health', methods=['GET'])
def health_check():
    """Server ishlayotganligini tekshirish"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'users_count': len(users_db),
        'orders_count': len(orders_db)
    })

if __name__ == '__main__':
    # Development server
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    # Production uchun gunicorn ishlatish:
    # gunicorn -w 4 -b 0.0.0.0:5000 backend_server:app
