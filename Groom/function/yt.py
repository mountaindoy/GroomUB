from Groom import groom 
from pyrogram import filters
from os import path
from youtube_dl import YoutubeDL
from config import Config
from youtube_search import YoutubeSearch

audio_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

video_opts = {}


def ytdlsearch(query: str) -> str:
    try:
        results = json.loads(YoutubeSearch(query, max_results=7).to_json())
    except KeyError:
        return print("Unable to find relevant search queries...")
    output = ""
    for i in results["videos"]:
        output += ("https://www.youtube.com{i['url_suffix']}\n\n")
    await print(output)

    
    
def audiodl(url: str) -> str:
  info = ydl.extract_info(url, False)
  ydl = YoutubeDL(audio_opts)
  try:
    ydl.download([url])
  except Exception as e:
    print(e)
    await groom.send_message(Config.LOG_GROUP_ID, e)
        
        
        
def videodl(url: str) -> str:     
    with youtube_dl.YoutubeDL(video_opts) as ydl:
        ydl.download([url])
    except Exception as e:
        print(e)
        await groom.send_message(Config.LOG_GROUP_ID, e)
       
    

