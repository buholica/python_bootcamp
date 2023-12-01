import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

# Create a user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":  PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_response = requests.post(url=pixela_endpoint, json=user_params)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_params = {
    "id": PIXELA_GRAPH_ID,
    "name": "Steps Graph",
    "unit": "steps",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Create a pixel in the graph
today = datetime.now()
today_date = today.strftime("%Y%m%d")

pixel_post_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
pixel_post_params = {
    "date": today_date,
    "quantity": input("How many steps did you take today? "),
}

pixel_post_response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)

# Update the created pixel in the graph
pixel_update_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today_date}"
pixel_put_params = {
    "quantity": "2480",
}

pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_put_params, headers=headers)
print(pixel_update_response)

# Delete the created pixel in the graph
pixel_delete_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/20231128"
pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)