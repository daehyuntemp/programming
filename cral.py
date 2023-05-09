from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://news.naver.com/")
soup = BeautifulSoup(html, "html.parser")
news_link=soup.find_all('img')
for link in news_link:
    print(link.get('src'))