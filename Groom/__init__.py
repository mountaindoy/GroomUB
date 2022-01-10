import logging
import sys
import time
from pyrogram import Client, errors
from config import Config
import logging
from telegraph import Telegraph


# LOGGING
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)




# HELP CMD 
HELP = {}
CMD_HELP = {}



#UB START TIME OR UPTIME
StartTime = time.time()



# CLIENT
print("GROOM  :  STARTING GROOM UB CLIENT")
groom = Client(Config.SESSION, api_id=Config.API_ID, api_hash=Config.API_HASH)
groom.run()
print("GROOM BOT : STARTING GROOM ASSISTANT")
bot = Client(Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH)


# ABOUT USER
print("GROOM  :  GETTING USER INFO")
ME = app.get_me()
USER_ID = ME.id
USER_NAME = ME.first_name + (ME.last_name or "")
USER_USERNAME = ME.username
USER_MENTION = ME.mention
USER_DC_ID = ME.dc_id
print("GROOM  :  STARTED CLIENT as {USER_NAME}")



# TELEGRAPH 
telegraph = Telegraph()
telegraph.create_account(short_name=GROOMUB_{USER_NAME})
