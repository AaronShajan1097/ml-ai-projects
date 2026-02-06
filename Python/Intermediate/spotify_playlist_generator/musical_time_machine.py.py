from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.billboard.com/charts/hot-100/")

soup = BeautifulSoup(response.text, 'html.parser')

all_titles = soup.select("li ul li h3.c-title")

with open("E:/MY/Test/100 Songs Of October.txt", 'w') as file:
    i = 1
    for title in all_titles:
        file.write(f"({i}) {title.get_text(strip=True)}\n")
        i+= 1