import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# اطلاعات اختصاصی API خود را اینجا وارد کنید
API_ID = 38369797
API_HASH = "f96396f6eabe4018dc809f21c6314574"

# نام فایل سشن مربوط به این اکانت
SESSION_FILE = "Session1.text"

async def main():
    try:
        # خواندن رشته سشن از داخل فایل متنی
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            session_string = f.read().strip()
    except FileNotFoundError:
        print(f"❌ خطا: فایل {SESSION_FILE} پیدا نشد!")
        return

    # اتصال به تلگرام با استفاده از سشن ذخیره‌شده
    client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
    
    print("🔄 در حال اتصال به تلگرام...")
    await client.start()
    print("✅ با موفقیت به اکانت تلگرام متصل شد!")

    # تأخیر ۲.۵ ثانیه‌ای (قابل تنظیم برای کارهای دلخواه شما)
    await asyncio.sleep(2.5)

    # حلقه‌ی اصلی ربات (برای اینکه ربات همیشه روشن بماند و خاموش نشود)
    print("🤖 ربات در حال اجراست و آماده به کار است...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
