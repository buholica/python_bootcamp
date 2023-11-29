import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TWILIO_ACC_SID = os.getenv("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_PHONE_NUM = os.getenv("MY_PHONE_NUM")

weather_params = {
    "lat": 65.012093,
    "lon": 25.465076,
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_snow = False
for hour_data in weather_data["list"]:
    condition_id = hour_data["weather"][0]["id"]
    if 600 <= int(condition_id) < 700:
        will_snow = True

if will_snow:
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to snow today. Please, wear a hat, scarf, gloves and a charming smile ⛄😊❄️",
            from_='+14848519199',
            to=MY_PHONE_NUM
        )
    print(message.status)