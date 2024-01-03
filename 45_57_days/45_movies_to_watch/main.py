import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.content)
encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
parser = 'html.parser'
soup = BeautifulSoup(response.content, parser, from_encoding=encoding)

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")