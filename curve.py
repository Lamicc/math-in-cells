#python 3 script
import numpy as np
import matplotlib.pyplot as plt

# new-born cell number
def newborncells(t,gamma):
    pro = 1
    for k in range(1,t+1):
        pro = pro*(1+k/gamma)
    return (2**t)/pro

# probability of mortalization
def pm(t,gamma):
    return t/(gamma+t)

def rvpm(t,gamma):
    return gamma/(gamma+t)

# accumulated cell number
def accumulate(t,g):
    if t == 0:
        return 1
    else:
        cumsum = 1
        for i in range(1,t+1):
            cumsum += newborncells(i,g)*pm(i,g)
            #cumsum += newborncells(i,g)*rvpm(i,g)
        return cumsum

# examples

x = np.arange(0, 40, 1)
#rv14 = [rvpm(c,14) for c in x]
#rv24 = [rvpm(c,24) for c in x]
#rv38 = [rvpm(c,38) for c in x]
ny14 = [accumulate(c,14) for c in x]
ny24 = [accumulate(c,24) for c in x]
ny38 = [accumulate(c,38) for c in x]
plt.plot(x,ny14)
plt.plot(x,ny24)
plt.plot(x,ny38)
#plt.plot(x,rv14)
#plt.plot(x,rv24)
#plt.plot(x,rv38)
plt.semilogy()
#plt.xlim(xmin=0)
#plt.ylim(ymin=0)
plt.show()
