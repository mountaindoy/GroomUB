#admin.py
from pyrogram import Client, filters
from Groom import groom
from config import Config
from pyrogram.types import Message



@groom.on_message(filters.command("ban", PREFIX) & filters.me & filters.USER(Config.SUDO) & filters.group))
def ban(client: Client, message: Message):
	groom.delete_messages(message.chat.id, message.message.id)
	msg = await send_message("Banning...")
	uname = message.reply_to_message.from_user.mention
	groom.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	msg.edit_text(f"Done! Banned {uname}")


@groom.on_message(filters.command("unban", PREFIX) & filters.me & filters.USER(Config.SUDO) & filters.group))
def ban(client: Client, message: Message):
	groom.delete_messages(message.chat.id, message.message.id)
	msg = await send_message("Unbanning...")
	uname = message.reply_to_message.from_user.mention
	groom.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	msg.edit_text(f"Done! Unbanned {uname}")




@groom.on_message(filters.command("mute", PREFIX) & filters.me & filters.USER(Config.SUDO) & filters.group))
def ban(client: Client, message: Message):
	groom.delete_messages(message.chat.id, message.message.id)
	msg = await send_message("Muting...")
	uname = message.reply_to_message.from_user.mention
	groom.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	msg.edit_text(f"Done! Muted {uname}")


@groom.on_message(filters.command("unmute", PREFIX) & filters.me & filters.USER(Config.SUDO) & filters.group)
def ban(client: Client, message: Message):
	groom.delete_messages(message.chat.id, message.message.id)
	msg = await send_message("Unmuting...")
	uname = message.reply_to_message.from_user.mention
	groom.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
	msg.edit_text(f"Done! Unmuted {uname}")


@groom.on_message(filters.command("kickme", PREFIX) & filters.me & filters.USER(Config.SUDO) & filters.group)
def ban(client: Client, message: Message):
	groom.delete_messages(message.chat.id, message.message.id)
	msg = await send_message("Bye...See uhh in Hell...Ha Ha")
	groom.leave_chat(message.chat.id)



