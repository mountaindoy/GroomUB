from pyrogram import Client, filters
from Groom import bot
from config import Config
from pyrogram.types import Message
from Groom import USER_NAME


@bot.on_message(filters.command("start"))
def bot_start(client: Client, message: Message):
  await send_message("This is Groom UB Assistant")
