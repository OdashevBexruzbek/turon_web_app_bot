#!/bin/bash

# 🍽️ TURON KAFE BOT - AVTOMATIK SETUP SKRIPTI
# Bu skript serverni avtomatik sozlaydi

set -e  # Xatolik bo'lsa to'xtash

echo "🚀 Turon Kafe Bot Setup Boshlanmoqda..."
echo ""

# Ranglar
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Root tekshiruv
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Iltimos, root foydalanuvchi sifatida ishga tushiring (sudo bash setup.sh)${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Root ruxsati tekshirildi${NC}"

# 1. Sistema yangilanishi
echo ""
echo "📦 Sistema yangilanmoqda..."
apt update && apt upgrade -y
echo -e "${GREEN}✅ Sistema yangilandi${NC}"

# 2. Kerakli paketlar
echo ""
echo "📦 Kerakli paketlar o'rnatilmoqda..."
apt install -y python3 python3-pip python3-venv nginx certbot python3-certbot-nginx git ufw
echo -e "${GREEN}✅ Paketlar o'rnatildi${NC}"

# 3. Loyiha papkasi
echo ""
echo "📂 Loyiha papkasi yaratilmoqda..."
mkdir -p /var/www/turon_cafe
cd /var/www/turon_cafe
echo -e "${GREEN}✅ Papka yaratildi: /var/www/turon_cafe${NC}"

# 4. Virtual environment
echo ""
echo "🐍 Python virtual environment yaratilmoqda..."
python3 -m venv venv
source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment yaratildi${NC}"

# 5. Dependencies
echo ""
echo "📚 Python kutubxonalari o'rnatilmoqda..."
if [ -f "requirements_backend.txt" ]; then
    pip install -r requirements_backend.txt
else
    echo -e "${YELLOW}⚠️  requirements_backend.txt topilmadi, qo'lda o'rnating${NC}"
fi

if [ -f "requirements_bot.txt" ]; then
    pip install -r requirements_bot.txt
else
    echo -e "${YELLOW}⚠️  requirements_bot.txt topilmadi, qo'lda o'rnating${NC}"
fi
echo -e "${GREEN}✅ Kutubxonalar o'rnatildi${NC}"

# 6. .env fayl
echo ""
echo "🔐 .env fayl sozlanmoqda..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo -e "${YELLOW}⚠️  .env fayl yaratildi. Iltimos, sozlang: nano .env${NC}"
    else
        echo -e "${RED}❌ .env.example topilmadi!${NC}"
    fi
else
    echo -e "${GREEN}✅ .env fayl allaqachon mavjud${NC}"
fi

# 7. Nginx sozlash
echo ""
read -p "🌐 Domain name kiriting (example.com): " DOMAIN

if [ ! -z "$DOMAIN" ]; then
    echo ""
    echo "⚙️  Nginx konfiguratsiya yaratilmoqda..."
    
    cat > /etc/nginx/sites-available/turon_cafe << EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;

    # Frontend static files
    location / {
        root /var/www/turon_cafe;
        try_files \$uri \$uri/ =404;
    }

    # Backend API
    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }
}
EOF

    ln -sf /etc/nginx/sites-available/turon_cafe /etc/nginx/sites-enabled/
    nginx -t && systemctl restart nginx
    echo -e "${GREEN}✅ Nginx sozlandi${NC}"
    
    # SSL
    echo ""
    read -p "🔒 SSL sertifikat o'rnatishni xohlaysizmi? (y/n): " SSL_CHOICE
    if [ "$SSL_CHOICE" = "y" ] || [ "$SSL_CHOICE" = "Y" ]; then
        certbot --nginx -d $DOMAIN -d www.$DOMAIN
        echo -e "${GREEN}✅ SSL o'rnatildi${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Domain kiritilmadi, Nginx sozlanmadi${NC}"
fi

# 8. Systemd services
echo ""
echo "⚙️  Systemd servicelar yaratilmoqda..."

# Backend service
cat > /etc/systemd/system/turon_backend.service << EOF
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
EOF

# Bot service
cat > /etc/systemd/system/turon_bot.service << EOF
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
EOF

systemctl daemon-reload
systemctl enable turon_backend
systemctl enable turon_bot

echo -e "${GREEN}✅ Servicelar yaratildi${NC}"

# 9. Firewall
echo ""
echo "🔥 Firewall sozlanmoqda..."
ufw allow 22
ufw allow 80
ufw allow 443
yes | ufw enable
echo -e "${GREEN}✅ Firewall sozlandi${NC}"

# 10. Fayl ruxsatnomalari
echo ""
echo "🔐 Fayl ruxsatnomalari sozlanmoqda..."
chown -R www-data:www-data /var/www/turon_cafe
chmod -R 755 /var/www/turon_cafe
echo -e "${GREEN}✅ Ruxsatnomalar sozlandi${NC}"

# Tugadi!
echo ""
echo "════════════════════════════════════════════════════"
echo -e "${GREEN}✅ SETUP MUVAFFAQIYATLI TUGADI! 🎉${NC}"
echo "════════════════════════════════════════════════════"
echo ""
echo "📋 KEYINGI QADAMLAR:"
echo ""
echo "1. .env faylni sozlang:"
echo "   nano /var/www/turon_cafe/.env"
echo ""
echo "2. BOT_TOKEN va ADMIN_ID ni kiriting"
echo ""
echo "3. Servicelarni ishga tushiring:"
echo "   systemctl start turon_backend"
echo "   systemctl start turon_bot"
echo ""
echo "4. Statusni tekshiring:"
echo "   systemctl status turon_backend"
echo "   systemctl status turon_bot"
echo ""
if [ ! -z "$DOMAIN" ]; then
    echo "5. Browserda ochib ko'ring: https://$DOMAIN"
    echo ""
fi
echo "📚 To'liq yo'riqnoma: /var/www/turon_cafe/SERVER_SETUP.md"
echo ""
echo "🐛 Muammo bo'lsa loglarni ko'ring:"
echo "   journalctl -u turon_backend -f"
echo "   journalctl -u turon_bot -f"
echo ""
echo "════════════════════════════════════════════════════"
echo -e "${GREEN}Omad! 🍽️${NC}"
echo "════════════════════════════════════════════════════"
