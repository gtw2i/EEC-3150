import numpy as np
from matplotlib import pyplot as plt

nPts = 100

x = np.random.uniform(0,2*np.pi,size=nPts)
y = np.sin(x)

#plt.plot(x,y)

ind = np.argsort(x)

plt.plot(x[ind],y[ind])