import os, usecsv, re
total=usecsv.opencsv('popSeoul.csv')
i=total[4:10]
k=[]
for j in i:
    if re.search('\d',j):
        k.append(int(re.sub(',','',j)))
    else:
        k.append(j)

print(k)
