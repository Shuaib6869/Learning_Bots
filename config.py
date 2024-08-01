import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 20673346 
API_HASH = "550722463068e61dafee7c7ff3c2bfde"
BOT_TOKEN = "7176466515:AAEQxM29csITPbC9wowec2uHgc9tuf7o7Vg"
MONGO_DB_URI = "mongodb+srv://sameerkhan223328274:sameerkhan223328274@cluster0.tbzyoh1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -4250217471
OWNER_ID = 6316548884

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/Learning_Bots",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+KcAkDAKEcn40NzVl")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+KcAkDAKEcn40NzVl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQE7c0IAj7kDZaasiPrTkpBFjmf0XS1Ojo70M5HGteRZw0dSab51cjot8JipNx0Mm6iKowOiHrJh4oD-lSmCG-u7Oaonp9wKm5naYcnFox8sL0q8zKzkNfeQRkwkmjkxWh1R7jdDMM0nH0qt2l7aaEFBIndo6qhMzrvmp7uiV2ux65qt_K-y8qnS3Tqgqxt8wCFDCsPZ8V0EuR36HKbMghLGiBYkEoHnL0dBj_22xD2cQTY5K8x6oOOfhMQLVgMWB-3E_lRjLPBrWVdRKdbCkswTjn4Xd0P7Ye9u8vt8N5o7oVptcjl5SbtMKR6KAjcgM3G_noG0P-qupIDDnoTL3vWkhX5wAAAAF4fuMUAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
STATS_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
STREAM_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/4f4f65ab1853f1fd6a5ba.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
