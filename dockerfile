# Официальный образ Python
FROM python:3.11-slim

# Обязательно, чтобы не ломался импорт
ENV PYTHONPATH=/app

# Рабочая директория
WORKDIR /app

COPY requirements.txt .


# Системные зависимости 
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Установка Chrome
RUN apt-get update && apt-get install -y wget \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Устанавливаем Python-зависимости
# Альтернатива без requirements.txt: RUN pip install --no-cache-dir pytest requests faker allure-pytest selenium
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта
COPY . .

# Команда для запуска тестов
CMD ["pytest", "-v", "--alluredir=./allure-results"]