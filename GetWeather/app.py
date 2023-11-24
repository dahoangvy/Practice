import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from unidecode import unidecode
from config import bot_token, API_KEY
from datetime import datetime, timedelta


def temp_Description(temp):
    if temp < 16:
        return "Lạnh quéo"
    elif 16 <= temp < 22:
        return "Mát mát lạnh lạnh cũng thích"
    elif 22 <= temp < 26:
        return "Trời này thích qué"
    elif 26 <= temp < 30:
        return "Cũng được hong nóng mà cũng hong mát"
    else:
        return "Chả thích trời như này! Lóng lắm"


def getWeather(city):

    KEY = API_KEY
    # Định dạng lại tham số đầu vào city
    city = unidecode(city.title())

    # API để get vĩ độ và kinh độ của thành phố
    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&appid={KEY}"

    # Get request lấy dữ liệu lat lon
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    repo_city = requests.get(url_city, headers)
    location = repo_city.json()[0]
    lat = location['lat']
    lon = location['lon']

    # Từ dữ liệu lat lon lấy được thêm vào API lấy dữ liệu thời tiết
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}"
    repo_weather = requests.get(url_weather, headers)
    weather = repo_weather.json()

    # Lấy dữ liệu từ API trả về
    main_weather = weather.get("weather")[0].get("main")
    description_weather = weather.get(
        "weather")[0].get("description").capitalize()
    temp_main = weather.get("main").get("temp") - 273.15
    temp_main = round(temp_main, 2)

    temp_description = temp_Description(temp_main)
    # Định dạng lại giờ và thay đổi lại múi giờ phù hợp
    sunrise_sys = weather.get("sys").get("sunrise")
    sunrise_sys = (datetime.utcfromtimestamp(
        sunrise_sys) + timedelta(hours=7)).strftime("%H:%M:%M")

    sunset_sys = weather.get("sys").get("sunset")
    sunset_sys = (datetime.utcfromtimestamp(
        sunset_sys) + timedelta(hours=7)).strftime("%H:%M:%M")

    result = f"\n- Nhiệt độ: {temp_main}: {temp_description}\n- Thời tiết: {main_weather}\n- Mô tả: {description_weather}\n- Mặt trời mọc lúc: {sunrise_sys}\n- Mặt trời lặn lúc: {sunset_sys}"

    return result


CONVERSATION_STATE = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hế luuuu! Nhập /weather để xem thời tiết nhoaaaa")


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Nhập tên thành phồ muốn xem thời tiết!! Nhanh cái tay lênnnn")

    # Đặt trạng thái cho cuộc trò chuyện là "waiting_for_city"
    CONVERSATION_STATE[update.message.chat_id] = "waiting_for_city"


app = ApplicationBuilder().token(bot_token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weather", weather))


async def handle_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Kiểm tra xem bot đang chờ người dùng nhập thành phố hay không
    if update.message.chat_id in CONVERSATION_STATE and CONVERSATION_STATE[update.message.chat_id] == "waiting_for_city":
        city = update.message.text
        # Gọi hàm getWeather với tham số thành phố
        weather_result = getWeather(city)

        # Gửi kết quả về cho người dùng
        await update.message.reply_text(f'Thời tiết ở {city}: {weather_result}')

        # Đặt trạng thái cuộc trò chuyện về trạng thái ban đầu
        CONVERSATION_STATE[update.message.chat_id] = None

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_city))

app.run_polling()
