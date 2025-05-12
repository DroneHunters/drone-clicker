import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from database import Database

# Настройки
TOKEN = os.getenv("7609819161:AAHr38bfzh8fhqx5KG3fM3tNUwgs_buQ1XA") or "7609819161:AAHr38bfzh8fhqx5KG3fM3tNUwgs_buQ1XA"
ADMIN_ID = 123456789  # Ваш Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
db = Database("drones.db")

# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if not db.user_exists(user_id):
        db.add_user(user_id)
    
    await message.answer(
        "🛸 *Drone Clicker* — собирай детали и улучшай дронов!\n\n"
        "🎮 Играть: /play\n"
        "👥 Рефералы: /ref\n"
        "💰 Рынок: /market",
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(
                "▶️ Играть", 
                web_app=WebAppInfo(url="https://DroneHunters.github.io/drone-clicker/web/")
            )
        )
    )

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)