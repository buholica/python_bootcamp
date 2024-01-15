import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

url = "https://www.amazon.com/Fujifilm-X-T5-Mirrorless-Digital-Camera/dp/B0BK2MW5HV/ref=sr_1_15?crid=2O7VSI7QKLR0I&keywords=fuji+digital+camera&qid=1704362365&s=photo&sprefix=fuji+%2Cphoto%2C170&sr=1-15"
headers = {
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
    "User-Agent": "Defined"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price_tag = soup.find(name="span", class_="a-price-whole")
# price_tag = "1,699.".strip(".")
price = int(price_tag.getText().strip('.').replace(",", '', 1))
# price = int(price_tag.replace(",", '', 1))
# print(price)

BUY_PRICE = 1800
item_title_tag = soup.find(name="h1", id="title")
item_title = item_title_tag.getText().strip()
print(item_title)

if price < BUY_PRICE:
    message = f"{item_title} is now ${price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))
else:
    print(f"Sorry, the item price is above ${BUY_PRICE}.")