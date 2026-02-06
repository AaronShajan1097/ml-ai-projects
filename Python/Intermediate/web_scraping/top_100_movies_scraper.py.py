from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movies_titles = soup.select(".content_content__i0P3p > h2 > strong")
movies_list = reversed([movie.getText() for movie in movies_titles])

with open("100_Movies_Of_All_Time.txt", 'w') as file:
    for movies in movies_list:
        file.write(f"{movies}\n")