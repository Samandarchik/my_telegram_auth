# Rasmdan Python 3.10 ishlatamiz
FROM python:3.10-slim

# Ishchi katalog
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani konteynerga ko‘chirish
COPY . .

# Skriptni ishga tushirish
CMD ["python", "main.py"]
