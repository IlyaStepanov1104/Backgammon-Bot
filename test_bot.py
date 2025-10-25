import asyncio
from aiogram import Bot, Dispatcher, types

from const import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    update = types.Update(update_id=0, message=message)

    webhook_json = update.model_dump_json(indent=2, exclude_none=True)
    print("📥 Webhook-style update JSON:")
    print(webhook_json)

    await message.answer("Получено! Смотри консоль для webhook JSON.")


@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    update = types.Update(update_id=0, callback_query=callback)

    webhook_json = update.model_dump_json(indent=2, exclude_none=True)
    print("📥 Webhook-style update JSON (callback_query):")
    print(webhook_json)

    await callback.answer("Нажатие обработано!")  # ответ в интерфейсе


# Запуск
async def main():
    print("🤖 Бот запущен через polling.")
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
