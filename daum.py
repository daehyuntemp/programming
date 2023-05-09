
import requests 			# 웹사이트에 HTTP 요청을 보내고 응답 데이터를 받는 라이브러리
from bs4 import BeautifulSoup  	#HTML 파싱 라이브러리

url='https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%9B%94%EB%B3%84%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94'
# url='https://www.daum.net/'
# headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
# response=requests.get(url, headers=headers)		#print(repon,se.text)로 데이터 확인 후 다음 작성
response=requests.get(url)		#print(repon,se.text)로 데이터 확인 후 다음 작성
webpage=response.text
#print(webpage)
soup=BeautifulSoup(webpage,'html.parser') 
		# html 태그 문서를 파싱한 결과 
result=soup.find_all("div",attrs={'class':"data_box"})
data=[]					#fav리스트 선언
for row in result:
    data.append(row.text)			#fav리스트에 추가
print(data)				#fav리스트 출력
