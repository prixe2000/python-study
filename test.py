import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import datetime

news='http://news.daum.net/'
soup=bs(ur.urlopen(news).read(),'html.parser')
nowDate=datetime.datetime.now()

f=open(nowDate.strftime("%Y-%m-%d_%H%M")+".txt","w")
for i in soup.find_all('div',{"class":"relate_thumb"}):
    try:
        f.write(i.text + '\n')
        #f.write(i.find_all('a')[0].get('href')+'\n') #하이퍼링크도 넣기
        soup2=bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
f.close()

#exe 파일 만들기 명령어 프롬프트 명령 
#pip install pyinstaller
#pyinstaller --onefile test.py