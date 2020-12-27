from bs4 import BeautifulSoup
import lxml
import requests


url = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all(name='h3', class_='title')

output = ''

my_movies = movies
# for movie in movies:
my_movies.reverse()

for movie in my_movies:
    output += f'{movie.getText()}\n'

with open("100 Best Movies.txt", "w") as movie_handle:
    movie_handle.writelines(output)

