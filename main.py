import httpx
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

# 🔑 TOKEN VA API KALITLARNI SHU YERGA YOZING
TELEGRAM_BOT_TOKEN = "8183633828:AAHT5ZZNnpOX42PxgwSUx8uF32dqdYljae0"  # ← Bot token
AI_API_KEY = "8e6e5f0c6865442cab5d3216dba1b344"                            # ← OpenAI token
AI_API_URL = "https://api.openai.com/v1/chat/completions"    # ← API URL
ADMIN_ID = 5311333610                                         # ← Admin ID

# 📁 Foydalanuvchini ro'yxatga olish
def add_user(user_id: int):
    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
    except FileNotFoundError:
        users = []

    if str(user_id) not in users:
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

# 🤖 AI API so‘rov (asinxron)
async def ask_ai(user_message: str) -> str:
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4",  # yoki "gpt-3.5-turbo", yoki siz yozgan model
        "messages": [{"role": "user", "content": user_message}],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(AI_API_URL, headers=headers, json=payload)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return (
            "⚠️ Kechirasiz, Limitingiz to‘ldi.\n"
            "1 soatdan keyin qayta urinib ko‘ring.\n"
            "Muammo haqida @Muttaqiyn_Dev ga xabar bering."
        )

# 🧠 AI savol-javob
async def handle_message(message: Message, bot: Bot):
    add_user(message.from_user.id)
    await message.answer("⏳ Yozilyapti...")
    ai_reply = await ask_ai(message.text)
    await message.answer(ai_reply, parse_mode=ParseMode.HTML)

# /start komandasi
async def start_cmd(message: Message):
    await message.answer(
        "🎉 Assalomu alaykum xush kelibsiz!\n Men ChatGPT asosidagi sun’iy intellekt yordamchiman —\n @Muttaqiyn_dev Tomonidan yaratilganman!\n\n 🤖 Sizga kerakli ma’lumotlarni topishga, savollaringizga javob berishga va foydali maslahatlar bilan yordam berishga har doim tayyorman.\n\n📝 Savolingiz bormi? Marhamat, yozing!"
    )

# /id komandasi
async def id_cmd(message: Message):
    await message.answer(f"Sizning Telegram ID'ingiz: `{message.from_user.id}`", parse_mode="Markdown")

# /users komandasi (admin uchun)
async def users_cmd(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("⛔ Bu buyruq faqat admin uchun!")

    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
        await message.answer(f"👥 Jami foydalanuvchilar soni: {len(users)} ta")
    except:
        await message.answer("Foydalanuvchilar ro‘yxati topilmadi.")

# /sendall komandasi
async def sendall_cmd(message: Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("⛔ Bu buyruq faqat admin uchun!")

    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        return await message.answer("❗ Yuboriladigan xabarni yozing. Masalan: /sendall Assalomu alaykum!")

    msg = text[1]

    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
    except:
        return await message.answer("❌ Hozircha hech kim yo‘q.")

    sent = 0
    for user_id in users:
        try:
            await bot.send_message(chat_id=int(user_id), text=msg)
            sent += 1
        except:
            continue

    await message.answer(f"✅ {sent} ta foydalanuvchiga xabar yuborildi.")

# 🚀 Botni ishga tushurish
async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    # 🧩 Handlerlar
    dp.message.register(start_cmd, Command("start"))
    dp.message.register(id_cmd, Command("id"))
    dp.message.register(users_cmd, Command("users"))
    dp.message.register(sendall_cmd, Command("sendall"))
    dp.message.register(handle_message, F.text & ~F.via_bot)

    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
