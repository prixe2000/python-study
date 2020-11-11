import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

#url='http://quotes.toscrape.com/'
#html=ur.urlopen(url)
#soup=bs(html.read(),'html.parser')
#밑에 한줄로 표현식

soup=bs(ur.urlopen('http://quotes.toscrape.com/').read(),'html.parser')
qoute=soup.find_all('div',{"class":"quote"}) #class속성값이 quote 인<div> 태그에 들어있는 텍스트 불러오기
result=[]
for i in qoute:
    result.append(i.text)

usecsv.writecsv('qoute.csv',result)