import os, requests
from pyrogram import Client, filters
from pyrogram.types import Message
from config import *
from downloader import process_link

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

STATS = {"processed":0,"success":0,"failed":0}

def update_dashboard():
    try:
        requests.post("http://127.0.0.1:8000/update", json=STATS, timeout=3)
    except:
        pass

app = Client(
    "ultra-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, m: Message):
    await m.reply("🔥 Ultra TXT Uploader Bot\n\nSend .txt file\nAdmin only.")

@app.on_message(filters.document & filters.private)
async def txt_handler(_, m: Message):
    if m.from_user.id != ADMIN_ID:
        return await m.reply("⛔ Admin only")

    if not m.document.file_name.endswith(".txt"):
        return await m.reply("❌ Send only .txt file")

    msg = await m.reply("📥 Downloading TXT...")
    path = await m.download()

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        links = [i.strip() for i in f if i.strip().startswith("http")]

    total = len(links)
    await msg.edit(f"📄 Total links: {total}")

    count = 1
    for link in links:
        STATS["processed"] += 1
        update_dashboard()

        status = await m.reply(f"⬇️ Processing {count}/{total}")
        file, time_taken = await process_link(link, count)

        if file:
            await status.edit("📤 Uploading...")
            await m.reply_video(file, caption=f"✅ Video {count}\n⏱ {time_taken}s")
            os.remove(file)
            STATS["success"] += 1
        else:
            await status.edit("❌ Failed")
            STATS["failed"] += 1

        update_dashboard()
        count += 1

    await m.reply("🎉 All tasks completed")

app.run()

