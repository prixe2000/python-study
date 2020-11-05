import os, re, codecs
os.chdir(r'C:\Beom Cording\study\do-it-python-master\do-it-python-master\03')
f=codecs.open('friends101.txt','r',encoding='utf-8')
script=f.read()
line=re.findall(r'Monica:.+',script)
f.close()


os.chdir(r'C:\Beom Cording\study')
f=codecs.open('Monica.txt','w',encoding='utf-8')
Monica=""
for i in line:
    Monica+=i
f.write(Monica)
f.close()