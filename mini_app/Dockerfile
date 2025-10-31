# Dockerfile
FROM node:20-alpine

WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь проект
COPY . .

# Переменные окружения
ENV NODE_ENV=production

# Открываем порт
EXPOSE 3000

# Команда запуска
CMD ["npm", "run", "dev"]
