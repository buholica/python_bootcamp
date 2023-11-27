import requests
from twilio.rest import Client
import os

api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
weather_params = {
    "lat": 49.99361,
    "lon": 31.56333,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_snow = False
for hour_data in weather_data["list"]:
    condition_id = hour_data["weather"][0]["id"]
    if 600 < int(condition_id) < 700:
        will_snow = True

if will_snow:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to snow today. Please, wear a hat, scarf, gloves and a charming smile ⛄😊❄️",
            from_='+14848519199',
            to='+380956530455'
        )
    print(message.status)