import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1").text

soup = BeautifulSoup(r, "html.parser")

title = soup.select('.lister-list .titleColumn a')
year = soup.select('.lister-list .titleColumn span')
rating = soup.select('.lister-list .ratingColumn strong')

with open("IMDB.csv", "w") as file:
    file.writelines(f"Title, Year, Rating\n")
    for i in range(len(title)):
        file.writelines(f"{title[i].text.replace(',','')},"
                        f" {year[i].text.replace('(', '').replace(')', '')},"
                        f" {rating[i].text}\n")
