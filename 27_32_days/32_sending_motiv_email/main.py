import smtplib
import random
import datetime as dt

MY_EMAIL = "oxanachyrkova9@gmail.com"
MY_PASSWORD = "test test test test"

today = dt.date.today()
day_of_week = today.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="test@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")