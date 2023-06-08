#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28668493
API_HASH = "2b1e2f6ea072d7dad084ab60ad4d7c3f"
BOT_TOKEN = "6098511840:AAEJCGq-X87udsls7W8KxJXfyTEI3c55Sh0"
SESSION = "BABsj6fuv3JWZb0y4Vuj33N_ovbn3Qxl0I28KIqWDyUjsWteriS9KQ7gdquLAy1pMWjhZTEwN2BaEpWfnH0qGtw3FHPGQ2rClvr38UZvDNEhCALs-N-kEzYiy09FW3vdhgk9ScNaxXHUTbxrvHOJ9fCBLNMBVoiprRtBnkNo0nTh7m5WYw9Kg9nnw6_gMWG7cZ8lWg1oIXnicOEZh7tlD6EBEtnLDz5fd6zRJgc1LLfFHlMF-OpmeFllA7sbhzFtlG3jQlK8pjKqYWtbNiMTOd-2gc53xdzph4GiAsB7ilCnjqg9kQTttSBiI_NqRcTV6agvfe-ZvOPZRw0xghBa34MrBXqFnQA"
FORCESUB = "Dronebots"
AUTH = 6098511840

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
