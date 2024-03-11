import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

data = soup.find_all(name="h3", class_="title")

movies=[]

for m in data:
    movie = m.getText()
    movies.append(movie)
movies.reverse()
print(movies)