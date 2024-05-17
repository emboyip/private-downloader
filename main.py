from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
import os
import random
import string
import zipfile
import shutil

plugin = dict(root="plugin")

app = Client(
    name="Privet_Downloader",
    api_id=123,
    api_hash="",
    phone_number="",
    plugins=plugin,
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

if os.path.exists("photo") and os.path.exists("video") and os.path.exists("music") and os.path.exists("voice") and os.path.exists("file"):
    pass
else:
    os.makedirs("photo")
    os.makedirs("video")
    os.makedirs("music")
    os.makedirs("voice")
    os.makedirs("file")


@app.on_message(filters.command("start" , "!") & filters.user(6629573141) , group=0)
async def get_all_channels(c: Client, m: Message):
    channel_info = ""
    async for channel in c.get_dialogs():
        if channel.chat.type == ChatType.CHANNEL:
            name = channel.chat.title
            chat_id = channel.chat.id
            channel_info += f"\nName: {name}\nID: {chat_id}\n\n"
    await m.reply_text("Which channel do you want to download?\n"+channel_info+"\n Exmple Download: [!down id]")


@app.on_message(filters.command("down" , "!") & filters.user(6629573141) , group=1)
async def Download(c:Client , m:Message):
    history = c.get_chat_history(chat_id=m.text.split(" ")[1])
    msg = await c.edit_message_text(m.chat.id , m.id , "Start Downloading")
    async for download in history:
        if download.photo:
            random_name = generate_random_string(5)
            if os.path.exists("photo/"+str(download.chat.id)):
                await c.download_media(download , f"photo/{str(download.chat.id)}/"+random_name+".jpg" , progress=progress)
            else:
                os.makedirs("photo/"+str(download.chat.id))
                await c.download_media(download , f"photo/{str(download.chat.id)}/"+random_name+".jpg", progress=progress)
        elif download.video:
            random_name = generate_random_string(5)
            if os.path.exists("video/"+str(download.chat.id)):
                await c.download_media(download , f"video/{str(download.chat.id)}/"+random_name+".mp4", progress=progress)
            else:
                os.makedirs("video/"+str(download.chat.id))
                await c.download_media(download , f"video/{str(download.chat.id)}/"+random_name+".mp4", progress=progress)
        elif download.audio:
            if os.path.exists("music/"+str(download.chat.id)):
                await c.download_media(download , f"music/{str(download.chat.id)}/"+download.audio.title+".mp3", progress=progress)
            else:
                os.makedirs("music/"+str(download.chat.id))
                await c.download_media(download , f"music/{str(download.chat.id)}/"+download.audio.title+".mp3", progress=progress)
        elif download.voice:
            if os.path.exists("voice/"+str(download.chat.id)):
                await c.download_media(download , f"voice/{str(download.chat.id)}/"+random_name+".ogg", progress=progress)
            else:
                os.makedirs("voice/"+str(download.chat.id))
                await c.download_media(download , f"voice/{str(download.chat.id)}/"+random_name+".ogg", progress=progress)
        elif download.document:
            if os.path.exists("file/"+str(download.chat.id)):
                await c.download_media(download , f"file/{str(download.chat.id)}/"+download.document.file_name, progress=progress)
            else:
                os.makedirs("file/"+str(download.chat.id))
                await c.download_media(download , f"file/{str(download.chat.id)}/"+download.document.file_name, progress=progress)
    await c.edit_message_text(m.chat.id , msg.id , "🤑End Downloading \n\nif you need file now \n send [!photo , !video , !music , !document , !voice] and wait \n\n Exmple Send: !photo id")



@app.on_message(filters.command("photo" , "!") & filters.user(6629573141) , group=2)
async def Send_photo(c:Client , m:Message):
    chanel_id = m.text.split(" ")[1]
    dir_path = "photo/"+chanel_id
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'photo.zip')
    await c.delete_messages(m.chat.id , m.id)
    await m.reply_document("photo.zip" , caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree("photo/"+chanel_id)
    os.remove("photo.zip")

@app.on_message(filters.command("video" , "!") & filters.user(6629573141) , group=3)
async def Send_video(c:Client , m:Message):
    chanel_id = m.text.split(" ")[1]
    dir_path = "video/"+chanel_id
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'video.zip')
    await c.delete_messages(m.chat.id , m.id)
    await m.reply_document("video.zip" , caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree("video/"+chanel_id)
    os.remove("video.zip")

@app.on_message(filters.command("music" , "!") & filters.user(6629573141) , group=4)
async def Send_music(c:Client , m:Message):
    chanel_id = m.text.split(" ")[1]
    dir_path = "music/"+chanel_id
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'music.zip')
    await c.delete_messages(m.chat.id , m.id)
    await m.reply_document("music.zip" , caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree("music/"+chanel_id)
    os.remove("music.zip")

@app.on_message(filters.command("file" , "!") & filters.user(6629573141) , group=5)
async def Send_file(c:Client , m:Message):
    chanel_id = m.text.split(" ")[1]
    dir_path = "file/"+chanel_id
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'file.zip')
    await c.delete_messages(m.chat.id , m.id)
    await m.reply_document("file.zip" , caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree("file/"+chanel_id)
    os.remove("file.zip")

@app.on_message(filters.command("voice" , "!") & filters.user(6629573141) , group=6)
async def Send_voice(c:Client , m:Message):
    chanel_id = m.text.split(" ")[1]
    dir_path = "voice/"+chanel_id
    files_to_zip = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    zip_files(files_to_zip, 'voice.zip')
    await c.delete_messages(m.chat.id , m.id)
    await m.reply_document("voice.zip" , caption="☠️For security, I converted the file to zip☠️")
    shutil.rmtree("voice/"+chanel_id)
    os.remove("voice.zip")



@app.on_message(filters.private & filters.voice , group=7)
async def Voice_downloader(c:Client , m:Message):
    print(m)
    if m.voice.ttl_seconds:
        voice = await m.download()
        await c.send_voice("me" , voice)
        os.remove(voice)


@app.on_message(filters.private & filters.photo , group=8)
async def Photo_downloader(c:Client , m:Message):
    if m.photo.ttl_seconds:
        photo = await m.download()
        await c.send_photo("me" , photo)
        os.remove(photo)


@app.on_message(filters.private & filters.video, group=9)
async def Video_downloader(c:Client , m:Message):
    if m.video.ttl_seconds:
        video = await m.download()
        await c.send_video("me" , video)
        os.remove(video)



app.run()
