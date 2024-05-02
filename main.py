from pyrogram import Client
from pyrogram.types import Message

plugin = dict(root="plugin")

app = Client(
    name="Privet_Downloader",
    api_id=26471977,
    api_hash="d79686c0a3ad440560c342c609dede66",
    phone_number="212703481994",
    plugins=plugin,
    device_model="Iphone 15 ProMax"
)

app.run()