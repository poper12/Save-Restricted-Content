# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20445873"))
API_HASH = getenv("API_HASH", "057fd0be9d7c38526b143c582bceb24b")
BOT_TOKEN = getenv("BOT_TOKEN", "7581892761:AAF28kuqZvP2Cte2OxQvbbJ_5mtn8x7AU0E")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7607741983").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://aarusdb:aarusdb@aarusdb.naqur.mongodb.net/?retryWrites=true&w=majority&appName=aarusdb")
LOG_GROUP = getenv("LOG_GROUP", "-1002489586500")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002178582432"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "9999"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
