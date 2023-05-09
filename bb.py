from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")
soup = BeautifulSoup(html, "html.parser")
# result=soup.find_all("div",attrs={"class":"temperature_text"})	# 태그명 속성값을 웹페이지 개발자도구(F12)의 소스 코드에서 확인하여 가져옴
result = soup.select_one(' div.temperature_text > strong')
print(result)
# data=[]					#fav리스트 선언
# for row in result:
#     data.append(row.text)			#fav리스트에 
# print(data)				#fav리스트 출력
