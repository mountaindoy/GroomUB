import os

class Config(object):
    API_HASH = os.getenv("API_HASH")
    API_ID = int(os.getenv("API_ID"))
    HEROKU_API = os.getenv("HEROKU_API")
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
    SESSION = os.getenv("PYROGRAM_SESSION")
    PREFIX = os.environ.get("PREFIX", ".")
    SUDO = list(map(int, getenv("SUDO").split()))
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID"))
    SUPPORT_GROUP = getenv("GROUP_SUPPORT", "GroomUB")
    UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "x3Support")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/x3Network/GroomUB")
    groom_version = "beta1.1"
    BOT_TOKEN = os.getenv("BOT_TOKEN")
