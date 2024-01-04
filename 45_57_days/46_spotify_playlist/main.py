from pprint import pprint

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

date_input = ''


def validate_date(date):
    global date_input  # global constant for date_text to be keyed in by user
    date_input = date
    today = datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.fromisoformat(date)
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD.")
        return False

    if date > today:
        print("Date must be in the past.")
        return False
    else:
        return True


while not validate_date(input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")):
    print("Please try again.")

url = f"https://www.billboard.com/charts/hot-100/{date_input}/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)

all_songs = soup.select(".o-chart-results-list__item h3.c-title")
song_titles = [song.getText().strip() for song in all_songs]
print(song_titles)


# Authentication to Spotify
token = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="https://example.com", scope="playlist-modify-private", show_dialog=True))
# results = sp.current_user_saved_tracks()
user_id = token.current_user()["id"]


song_uris = []
year = date_input.split("-")[0]
for song in song_titles:
    result = token.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Making a playlist
playlist = token.user_playlist_create(user=user_id, name=f"Billboard 100 {year}", public=False)

# Adding songs to playlist
token.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
