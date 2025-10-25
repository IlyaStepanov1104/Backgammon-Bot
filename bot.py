import asyncio
import os
import uuid
import aiofiles

from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ContentType
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from const import BOT_TOKEN, YOUR_BOT_USERNAME, WEB_APP_URL
from parser import parse_file  # ты генерируешь steps.json и картинки внутри неё

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привет! Отправь файл с логами игры в короткие нарды.")


@router.message(F.content_type == ContentType.DOCUMENT)
async def handle_file(message: Message):
    doc = message.document
    user_id = message.from_user.id

    # Генерируем уникальный hash-директорию
    dir_name = str(uuid.uuid4())
    os.makedirs(f"uploaded/{dir_name}", exist_ok=True)
    file_path = f"uploaded/{dir_name}/{doc.file_name}"

    await message.answer("Файл получен. Начинаю обработку...")

    # Сохраняем файл
    file = await bot.download(doc)
    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(file.read())

    await message.answer("Файл обработан. Начинаю подготовку к отображению...")

    # Парсим и создаём steps.json
    games = parse_file(file_path, dir_name)

    # Удаляем исходный файл после обработки
    os.remove(file_path)

    # Отправляем кнопку-ссылку на мини-апп
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"Открыть игру {game} 📲",
                              # web_app=WebAppInfo(url=f"{WEB_APP_URL}/{YOUR_BOT_USERNAME}/mini_app?startapp=hash:{dir_name}/{game}"))] for
                              web_app=WebAppInfo(url=WEB_APP_URL))] for
        game in games
    ])

    await message.answer(
        "Готово! Нажми кнопку ниже, чтобы открыть игру и просмотреть ходы.",
        reply_markup=keyboard
    )


# Запуск
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
