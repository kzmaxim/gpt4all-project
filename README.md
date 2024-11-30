GPT-4All Flask API

Это Flask-приложение, которое предоставляет API для общения с моделью GPT-4All. Проект использует модель "Meta-Llama-3-8B-Instruct.Q4_0.gguf" для генерации ответов на сообщения.

Описание
Этот проект предоставляет REST API, которое позволяет отправлять текстовые сообщения и получать ответы от модели GPT-4All. В проекте используется Flask и библиотека gpt4all для работы с моделью.

Установка
Для запуска проекта вам нужно установить Python и необходимые зависимости.

Клонируйте репозиторий
git clone https://github.com/yourusername/gpt4all-flask-api.git
cd gpt4all-flask-api

Создайте виртуальное окружение (необязательно, но рекомендуется) и активируйте его:
python3 -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows


Затем установите зависимости:
pip install -r requirements.txt


Скачайте модель GPT-4All
Модель будет загружена автоматически при запуске приложения, если вы используете подходящую модель (например, Meta-Llama-3-8B-Instruct.Q4_0.gguf). Убедитесь, что у вас есть достаточно места на диске (модель размером около 4.66 GB).

Запустите приложение
Чтобы запустить сервер Flask, выполните команду:
python app.py
По умолчанию сервер будет доступен по адресу http://localhost:5000.

Использование
Отправка сообщений через API
Вы можете отправить POST-запрос к API для получения ответа от модели. Пример использования через curl:
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'

  
Ответ будет выглядеть следующим образом:
{
  "response": "Привет, как дела? Я здесь, чтобы помочь вам!"
}
Пример запроса в коде (Python)
Вы также можете отправлять запросы с использованием Python:
import requests

url = "http://localhost:5000/api/chat"
data = {"message": "Как работает API?"}

response = requests.post(url, json=data)
print(response.json())


Структура проекта

gpt4all-flask-api/
│
├── app.py            # Основной файл с сервером Flask
├── requirements.txt  # Список зависимостей для установки
└── README.md         # Этот файл
Зависимости
Проект использует следующие зависимости:

Flask
gpt4all
requests (для взаимодействия с API)
Список зависимостей можно установить с помощью команды:

pip install -r requirements.txt
Лицензия
Этот проект лицензирован под MIT License - подробности можно найти в файле LICENSE.

