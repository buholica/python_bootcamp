import datetime as dt
import pandas, os, random, smtplib

MY_EMAIL = "oxanachyrkova9@gmail.com"
MY_PASSWORD = "test test test test"

# Checking if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
day_now = today.day
month_now = today.month

data_csv = pandas.read_csv("birthdays.csv")
data = data_csv.to_dict(orient="records")

# Creating a new letter and sending it if today == birthday_date
for dictionary in data:
    if month_now == dictionary["month"] and day_now == dictionary["day"]:
        name = dictionary["name"]
        email = dictionary["email"]

        # Choosing a random letter template
        random_letter = random.choice(os.listdir("letter_templates/"))
        with open(f"letter_templates/{random_letter}", encoding="UTF-8") as letter:
            letter_pattern = letter.read()
            new_letter_pattern = letter_pattern.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday!!!\n\n{new_letter_pattern}")