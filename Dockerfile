# Python 3.9 slim image ishlatamiz
FROM python:3.9-slim

# Ishchi papka yaratamiz
WORKDIR /app

# Kerakli kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir telethon requests

# Python faylini copy qilamiz
COPY main.py .

# Session fayllarini copy qilamiz
COPY myaccount.session .

# Konteyner ishga tushganda dasturni ishga tushiradi
CMD ["python", "main.py"]