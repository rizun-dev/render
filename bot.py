import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiohttp import web

# Telegram токен із змінних середовища
TOKEN = os.getenv(8497952308:AAEFIo2eikuLiifDjDWt0XMMgK6ihUAp0e0)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обробка команди /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт! Я ваш бот на Render!")

# Обробка всіх текстових повідомлень
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.reply(f"Ви написали: {message.text}")

# Webhook для Telegram
async def handle(request):
    update = Update(**await request.json())
    await dp.process_update(update)
    return web.Response(text="ok")

# Запуск веб-сервера на Render
if __name__ == "__main__":
    app = web.Application()
    app.router.add_post(f"/webhook/{TOKEN}", handle)  # webhook endpoint
    port = int(os.environ.get("PORT", 8000))          # Render дає порт через змінну
    web.run_app(app, host="0.0.0.0", port=port)
