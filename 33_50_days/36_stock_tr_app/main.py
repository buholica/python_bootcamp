import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_ALPHA_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_ACC_SID = os.getenv("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

MY_PHONE_NUM = os.getenv("MY_PHONE_NUM")

# STEP 1. When stock price increase/decreases by 5%
# between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

before_yesterday_data = data_list[1]
b_yesterday_closing_price = float(before_yesterday_data["4. close"])

difference = abs(yesterday_closing_price - b_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

average_of_num = (yesterday_closing_price + b_yesterday_closing_price) / 2
diff_percent = round((difference / average_of_num) * 100)
print(f"Result is {diff_percent}%")

if abs(diff_percent) > 3:
    # Get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday_data,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles_list = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: "
                                f"{article['description']}") for article in three_articles]

    # Send a separate message with each article's title and description to your phone number.
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles_list:
        message = client.messages \
            .create(
                body=article,
                from_='+14848519199',
                to=MY_PHONE_NUM
            )
        print(message.status)
