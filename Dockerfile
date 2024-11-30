# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем зависимости
WORKDIR /app
COPY . /app

# Устанавливаем необходимые пакеты
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Flask
EXPOSE 5000

# Запускаем приложение
CMD ["python3", "app.py"]

