import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
movies_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies = movies_list[::-1]

with open("movies.txt",mode="w") as file:
    for mov in movies:
        file.write(f"{mov}\n")
