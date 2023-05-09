import requests
from bs4 import BeautifulSoup #HTML 파싱 라이브러리
url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
html =requests.get(url)
soup =BeautifulSoup(html.text,"html.parser")
result=soup.find_all("div",attrs={"class":"temperature_text"}) 
# 태그명 속성값을 웹페이지 개발자도구(F12)의 소스 코드에서 확인하여 가져옴
data=[]
for row in result:
    data.append(row.text) 
print(data)
