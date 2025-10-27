# Backgammon Bot - Анализатор игр в короткие нарды

Веб-приложение для анализа логов игр в короткие нарды с возможностью интерактивной визуализации ходов.

## Основные возможности

- Прием логов игры в виде текстового файла
- Парсинг и анализ ходов игры
- Генерация визуализации позиций шашек
- Отображение статистики и счета
- Интерактивный просмотр игры

## Технологический стек

- **Frontend**: 
  - Next.js (основное приложение)
  - TypeScript
  - React

- **Backend API**:
  - Next.js API Routes
  - Обработка файлов на сервере

## Структура проекта

```
Backgammon-Bot/
├── mini_app/            # Основное приложение Next.js
│   ├── src/
│   │   ├── app/         # Next.js роуты
│   │   ├── components/  # React компоненты
│   │   └── lib/         # Вспомогательные функции
├── json/                # Директория для сохранения игр
├── Dockerfile           # Конфигурация для Docker
└── README.md            # Документация
```

## Установка и запуск

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/IlyaStepanov1104/Backgammon-Bot.git
cd Backgammon-Bot/mini_app
```

2. Установите зависимости:
```bash
npm install
```

3. Настройте окружение:
```bash
cp .env.example .env
```

4. Запустите приложение:
```bash
npm run dev
```

### Деплой с помощью Docker

1. Соберите Docker образ:
```bash
docker build -t backgammon-bot .
```

2. Запустите контейнер:
```bash
docker run -d \
  -p 3000:3000 \
  -v $(pwd)/json:/app/json \
  --name backgammon-bot \
  backgammon-bot
```

3. Для обновления:
```bash
docker stop backgammon-bot
docker rm backgammon-bot
docker build -t backgammon-bot .
docker run -d \
  -p 3000:3000 \
  -v $(pwd)/json:/app/json \
  --name backgammon-bot \
  backgammon-bot
```

## Формат входных файлов

Приложение принимает текстовые файлы с логами игры в формате:
```
Player1: 5 Player2: 3
5 point match

Game 1
1) 11: 64/60 64/60   21: 64/60 64/60
2) 12: 64/60 64/60   22: 64/60 64/60
...
```

## Работа с ботом

Приложение предоставляет API эндпоинт `/api/bot` для пуллинга ботом. 