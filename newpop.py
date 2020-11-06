import os, usecsv, re
total=usecsv.opencsv('popSeoul.csv')

newpop=usecsv.switch(total)
new=[['구','한국인','외국인','외국인 비율(%)']]
for i in newpop:
    foreign=0
    try:
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        if foreign>3:
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass

usecsv.writecsv('newPOP.csv',new)