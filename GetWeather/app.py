import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from unidecode import unidecode

# bot_token = "6885700889:AAFtuuIMWBJrrbtD1sTSzyNFjxow6iWK6tU"

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# app = ApplicationBuilder().token(bot_token).build()

# app.add_handler(CommandHandler("hello", hello))
# app.run_polling()


def getWeather(city):
    city = unidecode(city.lower().replace(" ", "+"))
    url = f"https://www.google.com/search?q={city}+weather"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # time = soup.select('.wob_dts').text()
    # # info = soup.select('.wob_dc').text()
    temperature = soup.select('#wob_tm')[0].getText().strip()

    return temperature


print(getWeather("Hà Nội"))

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# urlrp = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Hello"
# requests.post(urlrp)
