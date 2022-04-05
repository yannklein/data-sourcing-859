import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'
response = requests.get(url, headers={ "Accept-Language": "en-US"}).content
# print(response)

soup = BeautifulSoup(response, 'html.parser')

# print(soup.title.text)

movies_list = []

movies = soup.find_all('div', class_='lister-item')
for movie in movies:
    title = movie.find("h3").find("a").text
    duration = movie.find("span", class_="runtime").text.strip(" min")
    movies_list.append({'title': title, 'duration': duration})

print(movies_list)