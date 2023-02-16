import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def make_list(movie_list):
    with open("movies.txt", mode="a", encoding="utf-8") as file:
        for movies in movie_list:
            file.write(f"{movies}\n")


response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")

movie = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

make_list(movie[::-1])
