# 1. Базовый образ
FROM node:20-alpine

# 2. Рабочая директория
WORKDIR /app

# 3. Копируем package.json и package-lock.json
COPY package*.json ./

# 4. Устанавливаем зависимости
RUN npm install

# 5. Копируем всё приложение
COPY . .

# 6. Открываем порт (по умолчанию Next.js dev слушает 3000)
EXPOSE 3000

# 7. Запускаем в dev-режиме
CMD ["npm", "run", "dev"]
