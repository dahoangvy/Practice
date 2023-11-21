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
    API_KEY = "729e9a6e05275c18609441979a14b651"
    city = unidecode(city.capitalize())
    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&appid={API_KEY}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    repo_city = requests.get(url_city,headers)
    location = repo_city.json()[0]
    lat = location['lat']
    lon = location['lon']
    city = location['name']


    url_weather = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API_KEY}"
    repo_weather = requests.get(url_weather, headers)
    weather = repo_weather
    return weather

print(getWeather("Ho Chi Minh"))

