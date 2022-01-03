from pyrogram import idle, Client, filters
from Groom import groom, LOGGER
from Groom.modules import *
import os
from config import Config
from pyrogram import __version__ as pyroversion
from Groom.modules import modules









async def start_ub():
    print(f"𝗚𝗥𝗢𝗢𝗠 𝗨𝗦𝗘𝗥𝗕𝗢𝗧")
    print(modules)
    restart_data = await clean_restart_stage()
    try:
        if restart_data:
            await groom.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted Successfully**",
            )

        else:
            await groom.send_photo(Config.LOG_GROUP_ID, "https://telegra.ph/file/e09ce38b1fe66f21d3787.jpg", "𝗚𝗥𝗢𝗢𝗠 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧𝗘𝗗\n\n`Groom Version` : `{Config.groom_version}`\n`Pyrogram Version` : `pyroversion`\n\n**Updates** : `[Groom Updates]({Config.UPDATES_CHANNEL})`\n**Support** : `[Groom Support]({Config.SUPPORT_GROUP})`", parse_mode="markdown")
    except Exception:
        pass
    await idle()
    await aiohttpsession.close()
    print("GROOM  :  CLOSING AIOHTTP SESSION AND STOPPING UB")
    await app.stop()
    print("GROOM  :  BYEE!")
    for task in asyncio.all_tasks():
        task.cancel()












if __name__ == "__main__":
    uvloop.install()
    try:
        try:
            loop.run_until_complete(start_ub())
        except asyncio.exceptions.CancelledError:
            pass
        loop.run_until_complete(asyncio.sleep(3.0)) # task cancel wait
    finally:
        loop.close()