from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOnline, UserStatusOffline, UserStatusRecently
import asyncio
import requests

# Shaxsiy akkaunt ma'lumotlari
api_id = 18821318
api_hash = "8ad61ff44aac22cfd36947dd1259ebd9"

# Bot token va xabar yuboriladigan user_id
BOT_TOKEN = "8157743798:AAELzxyyFLSMxbT-XL4l-3ZVmxVBXYOY0Ro"
SEND_TO_ID = 1066137436

# Kuzatiladigan foydalanuvchi ID
WATCH_ID = 7211692770

client = TelegramClient("myaccount", api_id, api_hash)

# Xabar yuborish funksiyasi
def send_via_bot(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": SEND_TO_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        print(f"Bot javob: {response.status_code}")
    except Exception as e:
        print("Xabar yuborishda xatolik:", e)

@client.on(events.UserUpdate)
async def handler(event):
    if event.user_id == WATCH_ID:
        try:
            # Status turini tekshirish
            if isinstance(event.status, UserStatusOnline):
                print("👤 Foydalanuvchi online!")
                send_via_bot("👤 Foydalanuvchi ONLINE bo'ldi!")
            elif isinstance(event.status, UserStatusOffline):
                print("👤 Foydalanuvchi offline!")
                send_via_bot("👤 Foydalanuvchi OFFLINE bo'ldi!")
            elif isinstance(event.status, UserStatusRecently):
                print("👤 Foydalanuvchi yaqinda online edi")
                send_via_bot("👤 Foydalanuvchi yaqinda ONLINE edi")
            else:
                print(f"👤 Foydalanuvchi holati: {type(event.status).__name__}")
                send_via_bot(f"👤 Foydalanuvchi holati o'zgarildi: {type(event.status).__name__}")
        except Exception as e:
            print(f"Handler xatolik: {e}")

async def main():
    print("🔍 Foydalanuvchi holati kuzatilyapti...")
    print(f"📱 Kuzatilayotgan ID: {WATCH_ID}")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())