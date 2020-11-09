import numpy as np, usecsv
quest=np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
quest[quest>5]=5
usecsv.writecsv('resultcsv.csv',quest)

