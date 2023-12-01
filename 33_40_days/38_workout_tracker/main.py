import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

NUTRIONIX_API_ID = os.getenv("NUTRIONIX_API_ID")
NUTRIONIX_API_KEY = os.getenv("NUTRIONIX_API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
DOC_ID = os.getenv("DOC_ID")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{DOC_ID}/workoutTracking/workouts"

exercise_headers = {
    "x-app-id": NUTRIONIX_API_ID,
    "x-app-key": NUTRIONIX_API_KEY,
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": "65",
    "height_cm": "167",
    "age": "25",
}

exercise_response = requests.post(exercise_endpoint, json=parameters, headers=exercise_headers)
exercise_data = exercise_response.json()

today = datetime.today()
today_date = today.strftime("%Y/%m/%d")
today_time = today.strftime("%X")

for exercise in exercise_data["exercises"]:
    sheety_data = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_data, headers=sheety_headers)

