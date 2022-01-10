from Groom import groom 
from pyrogram import filters
from os import path
from youtube_dl import YoutubeDL
from config import Config


audio_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}




def audiodl(url: str) -> str:
  info = ydl.extract_info(url, False)
  ydl = YoutubeDL(audio_opts)
  try:
    ydl.download([url])
    except Exception as e:
      print(e)
      await groom.send_message(Config.LOG_GROUP_ID, e)
