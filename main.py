from pyrogram import Client
from pyrogram.types import Message

plugin = dict(root="plugin")

app = Client(
    name="Privet_Downloader",
    api_id=1234,
    api_hash="",
    phone_number="",
    plugins=plugin,
    device_model="Iphone 15 ProMax"
)

app.run()
