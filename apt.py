import os, re, usecsv
apt=usecsv.switch(usecsv.opencsv('apt_201910.csv'))

new_list=[]

for i in apt:
    try:
        if  i[5] > 120 and i[-4] < 80000 and re.match("강원",i[0]):
            new_list.append([i[0],i[4],i[-4]])
    except:
        pass

usecsv.writecsv('over120_over3000.csv',new_list)

#i[5]>120 and i[-4]<80000 and
#re.match("강원",i[0]):