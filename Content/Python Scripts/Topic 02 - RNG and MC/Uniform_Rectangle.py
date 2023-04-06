import numpy as np
import matplotlib.pyplot as plt

nPts = 2000

xmin = -2
xmax =  3
ymin = -1
ymax = 2

x = np.random.uniform(xmin,xmax,nPts)
y = np.random.uniform(ymin,ymax,nPts)

plt.plot(x,y,'.',markersize=3)

plt.xlim(-5,5)
plt.ylim(-5,5)