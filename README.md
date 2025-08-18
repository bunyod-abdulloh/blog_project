📝 Django Blog Platform

Bu loyiha — Django framework yordamida yozilgan shaxsiy blog platformasi. Unda foydalanuvchilar post qo‘shishi, izoh qoldirishi, eng ko‘p ko‘rilgan va eng yangi postlarni ko‘rishi mumkin. Shuningdek, haftalik va oylik eng mashhur postlar ham ajratib ko‘rsatiladi.

🚀 Xususiyatlar

🔐 Foydalanuvchi ro‘yxatdan o‘tishi va login qilishi

➕ Post qo‘shish va tahrirlash

📰 Eng yangi postlar ro‘yxati

🔥 Eng ko‘p ko‘rilgan postlar

📅 Haftaning va oyni eng ommabop postlari

💡 Tavsiya qilingan postlar (ko‘p izohga ega bo‘lganlar)

💬 Postlarga izoh qoldirish

📷 Postga rasm qo‘shish

🎨 Bootstrap orqali chiroyli interfeys

🛠 Texnologiyalar

Python 3.x

Django

Bootstrap 5

SQLite (default) yoki boshqa DB (PostgreSQL, MySQL)

⚙️ O‘rnatish

Loyihani lokal kompyuteringizda ishga tushirish uchun quyidagi amallarni bajaring:

# Repozitoriyani klon qiling
git clone https://github.com/username/django-blog.git
cd django-blog

# Virtual environment yarating
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Zarur kutubxonalarni o‘rnating
pip install -r requirements.txt

# Migratsiyalarni bajaring
python manage.py migrate

# Superuser yarating
python manage.py createsuperuser

# Serverni ishga tushiring
python manage.py runserver

📂 Loyihaning asosiy struktura
blog_project/
│── blog/              # Asosiy app (posts, comments, views)
│── templates/blog/    # HTML fayllar (Bootstrap bilan)
│── static/blog/       # CSS, JS, Images
│── blog_project/      # Django settings va konfiguratsiya
│── manage.py
│── requirements.txt
│── README.md

👤 Foydalanuvchilar uchun

Ro‘yxatdan o‘tish va login qilish mumkin.

Postlarni o‘qish, ko‘rish va ularga izoh yozish mumkin.

Har bir postda ko‘rish soni avtomatik oshadi.

📸 Ekranlar

🏠 Home Page – eng yangi, ommabop va tavsiya qilingan postlar

🔑 Login/Register Page – foydalanuvchi autentifikatsiyasi

📰 Post Detail Page – post mazmuni va izohlar

🤝 Hissa qo‘shish

Agar loyihaga hissa qo‘shmoqchi bo‘lsangiz:

Repozitoriyani fork qiling

O‘z branch-ingizda ishlang (git checkout -b feature-name)

O‘zgarishlarni push qiling va pull request yuboring

📄 Litsenziya

Loyiha ochiq manbali va MIT license asosida tarqatiladi.