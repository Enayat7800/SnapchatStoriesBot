import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "28150346"))
    API_HASH = os.environ.get("API_HASH", "426f0d0a1da02dea8fb71cb0bd3ab7e1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6705357378:AAEFDCt40Hd1VziS4vSjnW1ZB1FHR6VX4LM")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Filestolinkmyfastbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start"]
