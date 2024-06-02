from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
import os
import random
import string
import zipfile
import shutil

plugin = dict(root="plugin")

admin = 111

app = Client(
    name="Privet_Downloader",
    api_id=111,
    api_hash="",
    phone_number="",
    device_model="Iphone 15 ProMax"
)

def zip_files(files, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

if not os.path.exists("photo"):
    os.makedirs("photo")
if not os.path.exists("video"):
    os.makedirs("video")
if not os.path.exists("music"):
    os.makedirs("music")
if not os.path.exists("voice"):
    os.makedirs("voice")
if not os.path.exists("file"):
    os.makedirs("file")

@app.on_message(filters.command("start", "!") & filters.user(admin), group=0)
async def get_all_channels(c: Client, m: Message):
    channel_info = ""
    async for channel in c.get_dialogs():
        if channel.chat.type == ChatType.CHANNEL:
            name = channel.chat.title
            chat_id = channel.chat.id
            channel_info += f"\nName: {name}\nID: {chat_id}\n\n"
    await m.reply_text("Which channel do you want to download?\n" + channel_info + "\n Example Download: [!down id]")

@app.on_message(filters.command("down", "!") & filters.user(admin), group=1)
async def Download(c: Client, m: Message):
    history = c.get_chat_history(chat_id=m.text.split(" ")[1])
    msg = await c.edit_message_text(m.chat.id, m.id, "Start Downloading")
    async for download in history:
        if download.photo:
            random_name = generate_random_string(5)
            if not os.path.exists(f"photo/{download.chat.id}"):
                os.makedirs(f"photo/{download.chat.id}")
            await c.download_media(download, f"photo/{download.chat.id}/{random_name}.jpg", progress=progress)
        elif download.video:
            random_name = generate_random_string(5)
            if not os.path.exists(f"video/{download.chat.id}"):
                os.makedirs(f"video/{download.chat.id}")
            await c.download_media(download, f"video/{download.chat.id}/{random_name}.mp4", progress=progress)
        elif download.audio:
            title = download.audio.title if download.audio.title else generate_random_string(5)
            if not os.path.exists(f"music/{download.chat.id}"):
                os.makedirs(f"music/{download.chat.id}")
            await c.download_media(download, f"music/{download.chat.id}/{title}.mp3", progress=progress)
        elif download.voice:
            random_name = generate_random_string(5)
            if not os.path.exists(f"voice/{download.chat.id}"):
                os.makedirs(f"voice/{download.chat.id}")
            await c.download_media(download, f"voice/{download.chat.id}/{random_name}.ogg", progress=progress)
        elif download.document:
            if not os.path.exists(f"file/{download.chat.id}"):
                os.makedirs(f"file/{download.chat.id}")
            await c.download_media(download, f"file/{download.chat.id}/{download.document.file_name}", progress=progress)
    await c.edit_message_text(m.chat.id, msg.id, "🤑End Downloading\n\nIf you need file now\nSend [!photo, !video, !music, !document, !voice] and wait\n\nExample Send: !photo id")

@app.on_message(filters.command("photo", "!") & filters.user(admin), group=2)
async def Send_photo(c: Client, m: Message):
    channel_id = m.text.split(" ")[1]
    dir_path = f"photo/{channel_id}"
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'photo.zip')
    await c.delete_messages(m.chat.id, m.id)
    await m.reply_document("photo.zip", caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree(dir_path)
    os.remove("photo.zip")

@app.on_message(filters.command("video", "!") & filters.user(admin), group=3)
async def Send_video(c: Client, m: Message):
    channel_id = m.text.split(" ")[1]
    dir_path = f"video/{channel_id}"
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'video.zip')
    await c.delete_messages(m.chat.id, m.id)
    await m.reply_document("video.zip", caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree(dir_path)
    os.remove("video.zip")

@app.on_message(filters.command("music", "!") & filters.user(admin), group=4)
async def Send_music(c: Client, m: Message):
    channel_id = m.text.split(" ")[1]
    dir_path = f"music/{channel_id}"
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'music.zip')
    await c.delete_messages(m.chat.id, m.id)
    await m.reply_document("music.zip", caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree(dir_path)
    os.remove("music.zip")

@app.on_message(filters.command("file", "!") & filters.user(admin), group=5)
async def Send_file(c: Client, m: Message):
    channel_id = m.text.split(" ")[1]
    dir_path = f"file/{channel_id}"
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'file.zip')
    await c.delete_messages(m.chat.id, m.id)
    await m.reply_document("file.zip", caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree(dir_path)
    os.remove("file.zip")

@app.on_message(filters.command("voice", "!") & filters.user(admin), group=6)
async def Send_voice(c: Client, m: Message):
    channel_id = m.text.split(" ")[1]
    dir_path = f"voice/{channel_id}"
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'voice.zip')
    await c.delete_messages(m.chat.id, m.id)
    await m.reply_document("voice.zip", caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree(dir_path)
    os.remove("voice.zip")

@app.on_message(filters.private & filters.voice, group=7)
async def Voice_downloader(c: Client, m: Message):
    if m.voice.ttl_seconds:
        voice = await m.download()
        await c.send_voice("me", voice)
        os.remove(voice)

@app.on_message(filters.private & filters.photo, group=8)
async def Photo_downloader(c: Client, m: Message):
    if m.photo.ttl_seconds:
        photo = await m.download()
        await c.send_photo("me", photo)
        os.remove(photo)

@app.on_message(filters.private & filters.video, group=9)
async def Video_downloader(c: Client, m: Message):
    if m.video.ttl_seconds:
        video = await m.download()
        await c.send_video("me", video)
        os.remove(video)

app.run()
