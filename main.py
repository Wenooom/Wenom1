import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# اطلاعات اختصاصی API شما
API_ID = 38369797
API_HASH = "f96396f6eabe4018dc809f21c6314574"

# نام فایل‌های شما در مخزن گیت‌هاب
SESSION_FILE = "Session1.text"
NUMBERS_FILE = "Number1.tex"

async def main():
    try:
        # خواندن رشته سشن از فایل
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            session_string = f.read().strip()
    except FileNotFoundError:
        print(f"❌ خطا: فایل سشن {SESSION_FILE} پیدا نشد!")
        return

    # اتصال به تلگرام
    client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
    
    print("🔄 در حال اتصال به تلگرام...")
    await client.start()
    print("✅ با موفقیت متصل شد! در حال خواندن اعداد...")

    try:
        # خواندن فایل اعداد
        with open(NUMBERS_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ خطا: فایل اعداد {NUMBERS_FILE} پیدا نشد!")
        return

    # ارسال خط به خط اعداد با تأخیر ۲.۵ ثانیه
    for line in lines:
        number = line.strip()
        if number:
            try:
                # ارسال به بخش پیام‌های ذخیره‌شده (Saved Messages) خود اکانت
                await client.send_message('me', number)
                print(f"📤 ارسال شد: {number}")
            except Exception as e:
                print(f"⚠️ خطا در ارسال {number}: {e}")
            
            # تأخیر ۲.۵ ثانیه‌ای بین هر ارسال
            await asyncio.sleep(2.5)

    print("🏁 ارسال تمام اعداد به پایان رسید!")
    
    # روشن نگه داشتن ربات بعد از اتمام ارسال
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
