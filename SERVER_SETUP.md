# 🚀 TURON KAFE BOT - SERVER SOZLASH YO'RIQNOMASI

## 📋 Kerakli narsalar:
1. VPS/Server (Ubuntu 20.04 yoki 22.04)
2. Domain name (ixtiyoriy, lekin tavsiya etiladi)
3. Telegram Bot Token (@BotFather dan)
4. Admin Telegram ID

## 📂 LOYIHA TUZILISHI:

```
turon_cafe_bot/
├── backend_server.py          # Flask backend
├── telegram_bot_webapp.py     # Telegram bot (Web App launcher)
├── turon_cafe_bot.py          # Telegram bot (Aiogram versiya)
├── turon_cafe_app_with_backend.html  # Frontend App
├── requirements_backend.txt   # Backend dependencies
├── requirements_bot.txt       # Bot dependencies
└── .env                       # Environment variables
```

## 🔧 1-BOSQICH: SERVER TAYYORLASH

### Ubuntu serverga kirish:
```bash
ssh root@your_server_ip
```

### Sistema yangilash:
```bash
sudo apt update && sudo apt upgrade -y
```

### Python va kerakli paketlar:
```bash
sudo apt install python3 python3-pip python3-venv nginx certbot python3-certbot-nginx -y
```

## 🔧 2-BOSQICH: LOYIHANI YUKLASH

### Loyiha papkasini yaratish:
```bash
mkdir -p /var/www/turon_cafe
cd /var/www/turon_cafe
```

### Virtual environment yaratish:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Fayllarni yuklash (Git orqali yoki SFTP):
```bash
# Git bilan:
git clone https://github.com/yourrepo/turon_cafe_bot.git .

# Yoki qo'lda fayl yuklash (SFTP/SCP):
# scp -r /local/path/* root@server_ip:/var/www/turon_cafe/
```

### Dependencies o'rnatish:
```bash
pip install -r requirements_backend.txt
pip install -r requirements_bot.txt
```

## 🔧 3-BOSQICH: KONFIGURATSIYA

### .env fayl yaratish:
```bash
nano .env
```

### .env fayl mazmuni:
```
BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_telegram_id
WEB_APP_URL=https://yourdomain.com/app
FLASK_SECRET_KEY=your_random_secret_key
```

### backend_server.py ni yangilash:
```bash
nano backend_server.py
```

`.env` fayldan o'qish uchun quyidagini qo'shing:
```python
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
```

## 🔧 4-BOSQICH: NGINX SOZLASH

### Nginx konfiguratsiya yaratish:
```bash
sudo nano /etc/nginx/sites-available/turon_cafe
```

### Nginx config:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Frontend static files
    location / {
        root /var/www/turon_cafe;
        try_files $uri $uri/ =404;
    }

    # Backend API
    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Konfiguratsiyani yoqish:
```bash
sudo ln -s /etc/nginx/sites-available/turon_cafe /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔧 5-BOSQICH: SSL SERTIFIKAT (HTTPS)

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## 🔧 6-BOSQICH: SYSTEMD SERVICE (24/7 ishlashi uchun)

### Backend service:
```bash
sudo nano /etc/systemd/system/turon_backend.service
```

```ini
[Unit]
Description=Turon Cafe Backend
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/turon_cafe
Environment="PATH=/var/www/turon_cafe/venv/bin"
ExecStart=/var/www/turon_cafe/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 backend_server:app

[Install]
WantedBy=multi-user.target
```

### Telegram Bot service:
```bash
sudo nano /etc/systemd/system/turon_bot.service
```

```ini
[Unit]
Description=Turon Cafe Telegram Bot
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/turon_cafe
Environment="PATH=/var/www/turon_cafe/venv/bin"
ExecStart=/var/www/turon_cafe/venv/bin/python telegram_bot_webapp.py

[Install]
WantedBy=multi-user.target
```

### Servicelarni yoqish:
```bash
sudo systemctl daemon-reload
sudo systemctl enable turon_backend
sudo systemctl enable turon_bot
sudo systemctl start turon_backend
sudo systemctl start turon_bot
```

### Statusni tekshirish:
```bash
sudo systemctl status turon_backend
sudo systemctl status turon_bot
```

## 🔧 7-BOSQICH: TELEGRAM BOT SOZLASH

### BotFather da Web App ni sozlash:
1. @BotFather ga boring
2. `/mybots` ni tanlang
3. Botingizni tanlang
4. "Menu Button" ni tanlang
5. "Configure Menu Button" ni bosing
6. Button nomini kiriting: "🍽️ Buyurtma"
7. Web App URL ni kiriting: `https://yourdomain.com/turon_cafe_app_with_backend.html`

## 📊 MONITORING VA LOGS

### Loglarni ko'rish:
```bash
# Backend logs
sudo journalctl -u turon_backend -f

# Bot logs
sudo journalctl -u turon_bot -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Servicelarni qayta ishga tushirish:
```bash
sudo systemctl restart turon_backend
sudo systemctl restart turon_bot
sudo systemctl restart nginx
```

## 🔒 XAVFSIZLIK

### Firewall sozlash:
```bash
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
sudo ufw enable
```

### Fayl ruxsatnomalari:
```bash
sudo chown -R www-data:www-data /var/www/turon_cafe
sudo chmod -R 755 /var/www/turon_cafe
```

## 🗄️ DATABASE (PRODUCTION UCHUN)

### PostgreSQL o'rnatish (tavsiya etiladi):
```bash
sudo apt install postgresql postgresql-contrib -y
```

### Database yaratish:
```bash
sudo -u postgres psql
CREATE DATABASE turon_cafe;
CREATE USER turon_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE turon_cafe TO turon_user;
\q
```

### Python da PostgreSQL:
```bash
pip install psycopg2-binary SQLAlchemy
```

## 📈 YANGILASH (UPDATE)

### Kodlarni yangilash:
```bash
cd /var/www/turon_cafe
git pull  # Yoki yangi fayllarni yuklang
sudo systemctl restart turon_backend
sudo systemctl restart turon_bot
```

## ⚡ TEZKOR DEPLOY (Docker bilan - IXTIYORIY)

### Dockerfile:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements_backend.txt .
RUN pip install -r requirements_backend.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "backend_server:app"]
```

### Docker Compose:
```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "5000:5000"
    environment:
      - BOT_TOKEN=${BOT_TOKEN}
      - ADMIN_ID=${ADMIN_ID}
    restart: always

  bot:
    build: .
    command: python telegram_bot_webapp.py
    environment:
      - BOT_TOKEN=${BOT_TOKEN}
    restart: always
```

## 🎯 TEST QILISH

1. Browser orqali: `https://yourdomain.com/turon_cafe_app_with_backend.html`
2. Telegram bot: `/start` buyrug'ini yuboring
3. Buyurtma bering va admin ga xabar kelishini tekshiring

## 📞 MUAMMOLAR VA YECHIMLAR

### Bot ishlamayapti:
```bash
sudo systemctl status turon_bot
sudo journalctl -u turon_bot -n 50
```

### Backend ishlamayapti:
```bash
sudo systemctl status turon_backend
sudo journalctl -u turon_backend -n 50
```

### Web App ochilmayapti:
1. HTTPS borligini tekshiring
2. CORS sozlanganligini tekshiring
3. Browser console loglarini ko'ring

## ✅ TAYYOR!

Endi botingiz 24/7 ishlaydi! 🎉

Buyurtmalar adminga tushaveradi va mijozlar qulay interfeys orqali buyurtma beradilar.
