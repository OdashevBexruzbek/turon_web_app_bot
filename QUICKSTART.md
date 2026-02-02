# ⚡ TEZKOR BOSHLASH - 5 DAQIQADA!

Bu qo'llanma eng tez yo'l bilan botni ishga tushirish uchun.

## 📱 1-VARIANT: ODDIY BOT (5 DAQIQA)

### Kerakli narsalar:
- ✅ Python 3.8+
- ✅ Telegram Bot Token

### Qadamlar:

```bash
# 1. Fayllarni yuklab oling
git clone https://github.com/yourrepo/turon_cafe_bot.git
cd turon_cafe_bot

# 2. Virtual environment (ixtiyoriy)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Dependencies
pip install aiogram

# 4. Bot tokenni kiriting
nano turon_cafe_bot.py

# 5. Quyidagilarni o'zgartiring:
BOT_TOKEN = "YOUR_BOT_TOKEN"  # @BotFather dan
ADMIN_ID = 123456789          # @userinfobot dan

# 6. Ishga tushiring!
python turon_cafe_bot.py
```

**TAYYOR!** Botingiz ishlamoqda! 🎉

Telegram'da botingizga `/start` yuboring va buyurtma bering!

---

## 🌐 2-VARIANT: WEB APP (30 DAQIQA)

### Kerakli narsalar:
- ✅ VPS/Server (Ubuntu)
- ✅ Domain name
- ✅ Telegram Bot Token

### Tezkor Setup:

```bash
# 1. Serverga ulanish
ssh root@YOUR_SERVER_IP

# 2. Fayllarni yuklash
wget https://github.com/yourrepo/turon_cafe_bot/archive/main.zip
unzip main.zip
cd turon_cafe_bot-main

# 3. Avtomatik setup (HAMMASI AVTOMATIK!)
sudo bash setup.sh

# Bu skript quyidagilarni qiladi:
# - Sistema yangilash
# - Python, Nginx o'rnatish
# - Virtual environment yaratish
# - Dependencies o'rnatish
# - Nginx sozlash
# - SSL sertifikat
# - Systemd services
# - Firewall

# 4. .env sozlash
nano .env

# Quyidagilarni kiriting:
BOT_TOKEN=your_bot_token
ADMIN_ID=your_telegram_id
WEB_APP_URL=https://yourdomain.com/turon_cafe_app_with_backend.html

# 5. Servicelarni ishga tushirish
systemctl start turon_backend
systemctl start turon_bot

# 6. Tekshirish
systemctl status turon_backend
systemctl status turon_bot
```

**TAYYOR!** Botingiz 24/7 ishlamoqda! 🎉

Browser'da: `https://yourdomain.com`

---

## 🔍 TEZKOR TEKSHIRISH

### Bot ishlamoqdami?
```bash
# Logs
journalctl -u turon_bot -f

# Status
systemctl status turon_bot
```

### Backend ishlamoqdami?
```bash
# Logs
journalctl -u turon_backend -f

# Status
systemctl status turon_backend

# Health check
curl http://localhost:5000/health
```

### Nginx ishlamoqdami?
```bash
nginx -t
systemctl status nginx
```

---

## 🐛 TEZKOR XATO YECHISH

### "Bot javob bermayapti"
```bash
# Bot qayta ishga tushirish
systemctl restart turon_bot

# Loglarni ko'rish
journalctl -u turon_bot -n 50
```

### "Web App ochilmayapti"
1. HTTPS borligini tekshiring
2. Domain DNS sozlamalarini tekshiring
3. Nginx restart: `systemctl restart nginx`

### "Admin ga xabar kelmayapti"
1. ADMIN_ID to'g'ri ekanligini tekshiring
2. Bot tokenni tekshiring
3. Backend ishlayotganligini tekshiring

---

## 📊 TEZKOR KOMANDALAR

```bash
# Statuslar
systemctl status turon_bot
systemctl status turon_backend
systemctl status nginx

# Restart
systemctl restart turon_bot
systemctl restart turon_backend
systemctl restart nginx

# Logs (real-time)
journalctl -u turon_bot -f
journalctl -u turon_backend -f
tail -f /var/log/nginx/error.log

# Code yangilash
cd /var/www/turon_cafe
git pull
systemctl restart turon_backend
systemctl restart turon_bot
```

---

## 💡 MASLAHATLAR

### Development (Test) uchun:
```bash
# Local serverda test qilish
python backend_server.py

# Yoki
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

### Production uchun:
- ✅ HTTPS majburiy
- ✅ .env faylni himoyalang
- ✅ Database o'rnating
- ✅ Backup qiling
- ✅ Monitoring o'rnating

---

## 🎯 KEYINGI QADAMLAR

1. **Mahsulotlarni sozlang** → `backend_server.py` yoki `turon_cafe_bot.py`
2. **Rasmlar qo'shing** → CDN yoki server'ga yuklab
3. **To'lov qo'shing** → Click, Payme integratsiya
4. **Admin panel** → Statistika va boshqaruv

---

## 📞 YORDAM KERAKMI?

- 📖 To'liq qo'llanma: [SERVER_SETUP.md](SERVER_SETUP.md)
- 📖 README: [README.md](README.md)
- 🐛 GitHub Issues
- 💬 Telegram: @your_support

---

**🍽️ Omad! Bot bilan ishlashdan zavqlaning!** 🎉
