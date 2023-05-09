from datetime import date
import requests
from bs4 import BeautifulSoup 
import datetime
now=datetime.datetime.now()
ymd=str(now.year)+str(now.month)+str(now.day)
print(ymd)
ymd=input('궁금한 급식날짜를입력하세요.예20200901>>>')
url='http://daehyun.hs.kr/daehyun-h/M01030701/list?ymd='+ymd 
response=requests.get(url)
webpage=response.text
soup=BeautifulSoup(webpage,'html.parser')
meal1=soup.find('a',{'href':'/daehyun-h/M01030701/list?ymd='+ymd})#텍스트만 meal1변수에 저장 
print(meal1.text) 