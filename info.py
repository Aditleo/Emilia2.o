import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS' ,'https://graph.org/file/f302b70be1aff72a61299.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1815282501').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001889022398').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP') 
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://UI:UI@cluster0.v2hf3we.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "6"))
START_MESSAGE = environ.get('START_MESSAGE', '<b>✅ Report Send Successful ✅\n\n👤 Rᴇᴘᴏʀᴛᴇᴅ ᴜsᴇʀ : {user}\n🆔 Rᴇᴘᴏʀᴛᴇᴅ ᴜsᴇʀ ɪᴅ : {iu}\n📝 Rᴇᴘᴏʀᴛ ᴛʀᴀᴄᴋ ɪᴅ : #Log1909754\n\n💬 ʀᴇᴘᴏʀᴛ ᴛᴇxᴛ : {sarch}\n\n⏲️ ʀᴇᴘᴏʀᴛ ᴛɪᴍᴇ : {tim}\n🗓️ ʀᴇᴘᴏʀᴛ ᴅᴀᴛᴇ : {dai}\n⛅ ʀᴇᴘᴏʀᴛ ᴅᴀʏ : {mento}</b>')
STARTE_MESSAGE = environ.get('STARTE_MESSAGE', '<b> Hi HeLOO</b>') 
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}")
PMFILTER = environ.get('PMFILTER', "False")
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = environ.get("BUTTON_LOCK", "True")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001889022398))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mkn_bots_updates')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
PM_IMDB = environ.get('PM_IMDB', "True")
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>📁 FɪʟᴇNᴀᴍᴇ :</b> <code>{file_name}</code>\n\n<b>=========== • ✠ • ==========\n👥 ɢʀᴏᴜᴘ : @cenEma9\n🎬 ᴄʜᴀɴɴᴇʟ : @film_housc\n=========== • ✠ • ==========</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🪁 <b>Tɪᴛɪʟᴇ :  <a href={url}>{title}</a></b>\n\n📋 <b>ɪɴғᴏ</b> : <code>{release_date}</code>\n\n🌟 <b>Rᴀᴛɪɴɢ : {rating} / 10 </b>\n<code>({rating} based on {votes} user ratings)</code>\n\n🎭 <b>Gᴇɴʀᴇ :  <a href={url}>{genres}</a></b>\n\n🎙 <b>Lᴀɴɢᴜᴀɢᴇ</b> : <code>{languages}</code>\n🏜 <b>Cᴏᴜɴᴛʀʏ</b> : <code>{countries}</code>\n\n<b><i>▣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  <a href=https://t.me/film_hous>CɪɴᴇᴍᴀCᴏᴍᴘᴀɴʏ</a> </i></b>") 
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#request force sub
REQ_SUB = bool(environ.get("REQ_SUB", True))
SESSION_STRING = environ.get("SESSION_STRING", "")

#reqest channel 
SUPPORT_CHAT_ID = environ.get("SUPPORT_CHAT_ID", "-1001822093025")
REQST_CHANNEL = environ.get("REQST_CHANNEL", "-1001822093025")






