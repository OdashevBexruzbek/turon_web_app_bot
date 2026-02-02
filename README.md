# 🍽️ TURON KAFE - TELEGRAM BUYURTMA BOTI

Turon kafesi uchun zamonaviy buyurtma bot tizimi. Mijozlar Telegram orqali oson va qulay buyurtma beradilar!

## ✨ XUSUSIYATLAR

### 🎯 Asosiy Funksiyalar:
- ✅ Foydalanuvchi ro'yxatdan o'tish (ism, familiya, telefon, manzil)
- 📱 Zamonaviy Web App interfeysi
- 🍔 6 ta kategoriya: Fast-food, Pitsa, Milliy taomlar, Shirinliklar, Ichimliklar, Non
- 💰 Mahsulot tafsilotlari va narxlar
- 🔔 Adminga real-time buyurtma xabarlari
- 🌐 24/7 avtomatik ishlash
- 🎨 Chiroyli dizayn va animatsiyalar

### 🔐 Xavfsizlik:
- HTTPS protokoli
- Ma'lumotlar bazasi bilan ishlash
- Admin ID tekshiruvi

## 📦 LOYIHA TUZILISHI

```
turon_cafe_bot/
│
├── 📄 README.md                              # Bu fayl
├── 📄 SERVER_SETUP.md                        # Server sozlash yo'riqnomasi
│
├── 🤖 TELEGRAM BOT VERSIYALARI:
│   ├── turon_cafe_bot.py                    # Aiogram - to'liq bot (1-variant)
│   ├── telegram_bot_webapp.py               # Mini App launcher (2-variant)
│   └── requirements_bot.txt                 # Bot dependencies
│
├── 🌐 WEB APP VERSIYALARI:
│   ├── turon_cafe_app.html                  # Oddiy frontend (test uchun)
│   └── turon_cafe_app_with_backend.html     # Backend bilan ishlaydi (tavsiya)
│
└── ⚙️ BACKEND:
    ├── backend_server.py                    # Flask API server
    └── requirements_backend.txt             # Backend dependencies
```

## 🚀 QAYSI VERSIYANI TANLASH?

### 1️⃣ VARIANT - Oddiy Aiogram Bot (turon_cafe_bot.py)
**Afzalliklari:**
- Oson sozlash
- Bitta fayl
- Tez ishga tushirish

**Kamchiliklari:**
- Oddiy Telegram interfeysi
- Cheklangan dizayn imkoniyatlari

**Qachon ishlatish:**
- Juda tez ishga tushirish kerak bo'lsa
- Oddiy bot yetarli bo'lsa

### 2️⃣ VARIANT - Web App + Backend (TAVSIYA!) ⭐
**Afzalliklari:**
- ✨ Juda chiroyli dizayn
- 📱 Zamonaviy interfeys
- 🚀 Tez va qulay
- 💾 Ma'lumotlar bazasi
- 📊 Statistika va hisobotlar

**Kamchiliklari:**
- Ko'proq sozlash kerak
- Server va domain kerak

**Qachon ishlatish:**
- Professional bot kerak bo'lsa
- Mijozlarga eng yaxshi tajriba bermoqchi bo'lsangiz

## ⚡ TEZKOR BOSHLASH

### 1-VARIANT: Oddiy Bot (5 daqiqa)

```bash
# 1. Fayllarni yuklab oling
git clone https://github.com/yourrepo/turon_cafe_bot.git
cd turon_cafe_bot

# 2. Virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Dependencies
pip install -r requirements_bot.txt

# 4. Bot tokenni kiriting
nano turon_cafe_bot.py
# BOT_TOKEN va ADMIN_ID ni o'zgartiring

# 5. Ishga tushiring
python turon_cafe_bot.py
```

### 2-VARIANT: Web App + Backend (30 daqiqa)

```bash
# 1. Serverga ulanish
ssh root@your_server_ip

# 2. Loyihani yuklash
mkdir -p /var/www/turon_cafe
cd /var/www/turon_cafe
git clone https://github.com/yourrepo/turon_cafe_bot.git .

# 3. Setup
./setup.sh  # Yoki qo'lda SERVER_SETUP.md ni bajaring

# 4. .env sozlang
nano .env
# BOT_TOKEN, ADMIN_ID, WEB_APP_URL

# 5. Servicelarni ishga tushiring
sudo systemctl start turon_backend
sudo systemctl start turon_bot
```

To'liq yo'riqnoma: [SERVER_SETUP.md](SERVER_SETUP.md)

## 🔧 SOZLASH

### Bot Token Olish:
1. Telegram da @BotFather ni oching
2. `/newbot` buyrug'ini yuboring
3. Bot nomini kiriting: "Turon Kafe"
4. Bot username kiriting: "turon_cafe_bot"
5. Tokenni saqlang

### Admin ID Topish:
1. @userinfobot ga "/start" yuboring
2. ID ni ko'chirib oling

### Domain Sozlash (2-variant uchun):
1. Domain provider da A record qo'shing
2. IP: serveringizning IP manzili
3. SSL sertifikat o'rnating (certbot)

## 📱 FOYDALANISH

### Mijoz uchun:
1. Botni ochish: `/start`
2. Web App tugmasini bosish
3. Ro'yxatdan o'tish
4. Mahsulot tanlash
5. Buyurtma berish

### Admin uchun:
- Har buyurtma uchun xabar keladi
- Xabarda mijoz va mahsulot ma'lumotlari
- Telefon orqali aloqaga chiqish

## 🎨 MAHSULOTLARNI SOZLASH

### `backend_server.py` yoki `turon_cafe_bot.py` da:

```python
PRODUCTS = {
    "fast_food": {
        "product_id": {
            "name": "Mahsulot nomi",
            "price": 25000,
            "description": "Tavsif",
            "image": "https://example.com/image.jpg"  # Ixtiyoriy
        }
    }
}
```

### Yangi kategoriya qo'shish:

```python
# Backend da
"new_category": {
    "item1": {...},
    "item2": {...}
}

# Frontend da
<div class="category-card" onclick="showCategory('new_category')">
    <div class="category-icon">🆕</div>
    <div>Yangi Kategoriya</div>
</div>
```

## 🗄️ MA'LUMOTLAR BAZASI

### Development (oddiy):
```python
users_db = {}  # Dict
orders_db = []  # List
```

### Production (tavsiya):
```python
# PostgreSQL yoki MongoDB
import psycopg2
# yoki
from pymongo import MongoClient
```

## 📊 MONITORING

### Loglar:
```bash
# Backend
sudo journalctl -u turon_backend -f

# Bot
sudo journalctl -u turon_bot -f
```

### Statistika:
```bash
curl http://localhost:5000/health
```

## 🔄 YANGILASH

```bash
cd /var/www/turon_cafe
git pull
sudo systemctl restart turon_backend
sudo systemctl restart turon_bot
```

## 🐛 MUAMMOLARNI YECHISH

### Bot javob bermayapti:
```bash
sudo systemctl status turon_bot
sudo journalctl -u turon_bot -n 50
```

### Web App ochilmayapti:
1. HTTPS borligini tekshiring
2. Domain to'g'ri sozlanganligini tekshiring
3. CORS yoqilganligini tekshiring

### Xabar kelmayapti:
1. ADMIN_ID to'g'ri ekanligini tekshiring
2. Bot tokenni tekshiring
3. Loglarni ko'ring

## 💡 KENGAYTIRISH G'OYALARI

### Yangi funksiyalar:
- 💳 Online to'lov (Click, Payme)
- 📍 Geolokatsiya
- ⭐ Mahsulotga baho berish
- 🎁 Aksiyalar va chegirmalar
- 📈 Admin panel
- 📱 Buyurtma holati tracking
- 🔔 Push bildirishnomalar
- 🤖 Chatbot yordamchi

### Integratsiyalar:
- Google Maps
- Payment systems
- CRM tizimlar
- Analytics (Google Analytics, Yandex Metrika)

## 📝 LITSENZIYA

MIT License - erkin foydalaning!

## 🤝 HISSA QO'SHISH

Pull request'lar xush kelibsiz! Katta o'zgarishlar uchun avval issue oching.

## 👨‍💻 MUALLIF

Sizning ismingiz
- Telegram: @your_username
- Email: your@email.com

## 🙏 MINNATDORCHILIK

- [Aiogram](https://docs.aiogram.dev/) - Telegram Bot framework
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Telegram](https://telegram.org/) - Platform

## ⚠️ ESLATMA

**Production uchun:**
1. ✅ Ma'lumotlar bazasi ishlating (PostgreSQL/MongoDB)
2. ✅ Environment variables ishlatishni unutmang
3. ✅ HTTPS majburiy
4. ✅ Backup strategiyasi yarating
5. ✅ Monitoring o'rnating
6. ✅ Error handling yaxshilang
7. ✅ Rate limiting qo'shing
8. ✅ Security testdan o'tkazing

**Xavfsizlik:**
- Hech qachon tokenlarni kodga qo'ymang
- .env faylni .gitignore ga qo'shing
- Parollarni hash qiling
- SQL injection dan himoyalaning
- XSS va CSRF dan himoyalaning

## 📞 YORDAM

Savol yoki muammo bo'lsa:
1. [GitHub Issues](https://github.com/yourrepo/turon_cafe_bot/issues)
2. Telegram: @your_support_username
3. Email: support@turoncafe.uz

---

⭐ Agar loyiha yoqsa, GitHub'da star bering!

🍽️ **Yaxshi ishlar va to'la buyurtmalar!**
