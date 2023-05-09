import re
import requests
from bs4 import BeautifulSoup 
url='https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'
# url='https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B040A3&checkFlag=N'
headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response=requests.get(url, headers=headers)
webpage=response.text
# print(webpage)
soup=BeautifulSoup(webpage,'html.parser')
result=soup.find_all('a',{'class':"tit_main"})
data=[]
for row in result:
    data.append(row.text)
print(data[0:5])