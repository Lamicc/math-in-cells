#python 3 script
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from curve import accumulate

# calculate accumulated cell number for data
def celnum(rateList):
    numList = []
    for i in range(len(rateList)):
        if i <1:
            numList.append(rateList[i])
        else:
            numList.append(numList[i-1]*rateList[i])
    return numList

# read data
y1 = pd.read_csv('Y01.csv')
y2 = pd.read_csv('Y02.csv')
y3 = pd.read_csv('Y03.csv')
y4 = pd.read_csv('Y04.csv')
y5 = pd.read_csv('Y05.csv')
y6 = pd.read_csv('Y06.csv')

li = [y1,y2,y3,y4,y5,y6]

# clean dataset
for i in range(len(li)):
    li[i] = li[i].drop(li[i].columns[0], axis=1)
    li[i] = li[i].T.reset_index()
    li[i].columns = li[i].iloc[0]
    li[i] = li[i].iloc[1:,:]
    li[i].loc[:,'rate'].replace(0, 1, inplace=True)
    li[i] = li[i].dropna(subset=['rate'])
    #print(li[i])
"""
# plot data
for i in range(len(li)):
    xdata = [d-3 for d in li[i].Days.astype('int')]
    plt.scatter(xdata,celnum(li[i].rate.tolist()),label='Y0'+str(i+1))
"""

#day = li[0].Days.astype('int')
day = li[1].Days.astype('int')
#day = li[2].Days.astype('int')
#day = li[3].Days.astype('int')
#day = li[4].Days.astype('int')
#day = li[5].Days.astype('int')

xdata = [d-3 for d in day]

#plt.scatter(xdata,celnum(li[0].rate.tolist()))
plt.scatter(xdata,celnum(li[1].rate.tolist()))
#plt.scatter(xdata,celnum(li[2].rate.tolist()))
#plt.scatter(xdata,celnum(li[3].rate.tolist()))
#plt.scatter(xdata,celnum(li[4].rate.tolist()))
#plt.scatter(xdata,celnum(li[5].rate.tolist()))


# plot curves
x = np.arange(0, 60, 1)

#ny0 = [accumulate(c,61) for c in x]
#plt.plot(x,ny0,label='gamma=61')

ny1 = [accumulate(c,50) for c in x]
plt.plot(x,ny1,label='gamma=50')

#ny2 = [accumulate(c,46) for c in x]
#plt.plot(x,ny2,label='gamma=46')

#ny3 = [accumulate(c,51) for c in x]
#plt.plot(x,ny3,label='gamma=51')

#ny4 = [accumulate(c,98) for c in x]
#plt.plot(x,ny4,label='gamma=98')

#ny5 = [accumulate(c,81) for c in x]
#plt.plot(x,ny5,label='gamma=81')

# figure attributes
plt.semilogy()
plt.xlim(xmin=0)
plt.ylim(ymin=1)
plt.xlabel('Time')
plt.ylabel('Accumulated cell number')
plt.legend()
#plt.title('Y06')
plt.show()
