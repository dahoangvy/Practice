import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

bot_token = "6885700889:AAFtuuIMWBJrrbtD1sTSzyNFjxow6iWK6tU"
chat_id = 855785263
url = "https://xoso.com.vn/xo-so-hom-qua.html"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# urlrp = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Hello"
# requests.post(urlrp)
