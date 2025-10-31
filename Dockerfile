# Используем официальный Node.js образ для Next.js приложения
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY mini_app/package*.json ./mini_app/

# Устанавливаем зависимости
RUN cd mini_app && npm install

# Копируем все файлы проекта
COPY . .

# Создаем необходимые директории
RUN mkdir -p /app/json

# Открываем порт для Next.js
EXPOSE 3000

# Запускаем приложение в dev режиме
CMD ["sh", "-c", "cd mini_app && npm run dev"]
