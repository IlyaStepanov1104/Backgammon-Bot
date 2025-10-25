# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости (предполагается, что у тебя есть requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Создаем папки для загрузок и изображений, чтобы бот мог их использовать
RUN mkdir -p uploaded images

# Указываем переменную окружения с токеном, если хочешь передавать в Docker run
# ENV BOT_TOKEN=your_bot_token_here

# Запускаем бота
CMD ["python", "bot.py"]
