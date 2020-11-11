import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news='http://news.daum.net/'
soup=bs(ur.urlopen(news).read(),'html.parser')
article=soup.find_all('div',{"class":"relate_thumb"})

for i in article: #헤드라인과 링크를 타고 들어가서 본문 갖고오기
    print(i.text,'\n') #헤드라인 들고오기
    soup3=bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')#하이퍼링크 안에 있는 기사 객체화
    for j in soup3.find_all('p'):#본문 갖고오기(본문 p클래스)
        print(j.text)

f=open('links.txt','w')  #하이퍼 링크 txt 파일로 만들기
for i in article:
    f.write(i.find_all('a')[0].get('href')+'\n')
f.close()

article1='https://news.v.daum.net/v/20201111103106157' #기사내용 txt 파일로 만들기
soup3=bs(ur.urlopen(article1).read(),'html.parser')
f=open('article1.txt','w')
for i in soup3.find_all('p'):
    f.write(i.text)

#최종 기사 제목, 본문, 하이퍼링크를 파일로 저장하기
news='http://news.daum.net/'
soup=bs(ur.urlopen(news).read(),'html.parser')
f=open('article_total.txt','w')
for i in soup.find_all('div',{"class":"relate_thumb"}):
    try:
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href')+'\n')
        soup2=bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
f.close()
