"""
Telegram Kanalimiz @Muttaqiyn_Media
Kanalimizga obuna bo'ling va boshqa dasturlarni o'tkazib yubormaysiz

Men bilan bog'lanish 
TELEGRAM: @MuttaqiynDev
"""

import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from google import generativeai

# # TOKEN VA API KALITLAR
TELEGRAM_BOT_TOKEN = "PUT-YOUR-TELEGRAM-BOT-TOKEN"
GEMINI_API_KEY = "PUT-YOUR-GEMINI_API_KEY"
ADMIN_ID = "PUT-TELEGRAM_ID"

# # Gemini sozlash
generativeai.configure(api_key=GEMINI_API_KEY)
model = generativeai.GenerativeModel('gemini-2.5-pro-exp-03-25')

#  Foydalanuvchilar DB
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)")
    conn.commit()
    conn.close()

def add_user(user_id: int):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users")
    users = [row[0] for row in c.fetchall()]
    conn.close()
    return users

# # Gemini AI bilan ishlash
async def ask_ai(user_message: str) -> str:
    try:
        response = model.generate_content(user_message)
        return response.text
    except Exception as e:
        return f"⚠️ Xatolik yuz berdi: {e}"

# # AI savol-javob
async def handle_message(message: Message, bot: Bot):
    add_user(message.from_user.id)
    await message.answer("⏳ Yozilyapti...")
    reply = await ask_ai(message.text)
    await message.answer(reply, parse_mode=ParseMode.HTML)

# # Commands
async def start_cmd(message: Message):
    user = message.from_user
    first_name = user.first_name
    user_id = user.id

    text = (
        f"🎉 Assalomu alaykum <a href='tg://user?id={user_id}'>{first_name}</a>, xush kelibsiz!\n"
        "Men ChatGPT asosidagi sun'iy intellekt yordamchiman —\n"
        "@Muttaqiyndev tomonidan yaratilganman!\n\n"
        "🤖 Sizga kerakli ma'lumotlarni topishga, savollaringizga javob berishga va foydali maslahatlar bilan yordam berishga har doim tayyorman.\n\n"
        "📝 Savolingiz bormi? Marhamat, yozing!"
    )

    await message.answer(text, parse_mode="HTML")

async def id_cmd(message: Message):
    await message.answer(f"Sizning Telegram ID'ingiz: `{message.from_user.id}`", parse_mode="Markdown")

async def users_cmd(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer(" Bu buyruq faqat admin uchun!")
    
    users = get_all_users()
    await message.answer(f"👥 Foydalanuvchilar soni: {len(users)} ta")

async def sendall_cmd(message: Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("⛔️ Bu buyruq faqat admin uchun!")

    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.answer("❗️ Xabarni yozing. Masalan: /sendall Assalomu alaykum!")

    msg = parts[1]
    users = get_all_users()
    sent = 0

    for user_id in users:
        try:
            await bot.send_message(chat_id=user_id, text=msg)
            sent += 1
        except:
            continue

    await message.answer(f"✅ {sent} ta foydalanuvchiga yuborildi.")

# # Botni ishga tushurish
async def main():
    init_db()
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_cmd, Command("start"))
    dp.message.register(id_cmd, Command("id"))
    dp.message.register(users_cmd, Command("users"))
    dp.message.register(sendall_cmd, Command("sendall"))
    dp.message.register(handle_message, F.text & ~F.via_bot)

    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
