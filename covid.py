import re
import requests
from bs4 import BeautifulSoup 

url='https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84'
headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response=requests.get(url, headers=headers)
webpage=response.text
# print(webpage)
soup=BeautifulSoup(webpage,'html.parser')

resultX=soup.select("#jupCovid19Coll > div.coll_cont > div > div._cont_tab.cont_confirmed > div > div:nth-child(2) > div.cont_info > div.wrap_map.map_confirmed > div > ul > li.location_seoul.step5 > a")
X=[]
Y=[]
for row in resultX:
    X.append(row.text)

print(X)
# for row in resultY:
#     Y.append(row.text)
# cnt=len(Y)
# print(X[:cnt])
# print(Y)
