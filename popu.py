import requests
from bs4 import BeautifulSoup 
url='https://pythondojang.bitbucket.io/weather/observation/currentweather.html'
# url='https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B040A3&checkFlag=N'
headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response=requests.get(url, headers=headers)
webpage=response.text
print(webpage)
soup=BeautifulSoup(webpage,'html.parser')
meal1=soup.find('td',{'class':"first trHeader"})
print(meal1) 