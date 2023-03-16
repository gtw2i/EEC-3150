import numpy as np
from matplotlib import pyplot as plt

nPts = 1000

a = -2
b = 2

x = (b-a)*np.random.rand(nPts)+a
y = (b-a)*np.random.rand(nPts)+a

plt.plot(x,y,'b.')

xmin = -1.5
xmax = 1
ymin = -1
ymax = 0.9

mask1 = x>xmin
mask2 = x<xmax
mask3 = y>ymin
mask4 = y<ymax

mask = np.logical_and(mask1,mask2)
mask = np.logical_and(mask,mask3)
mask = np.logical_and(mask,mask4)

x2 = x[mask]
y2 = y[mask]

print(x2.shape)

plt.plot(x2,y2,'rx',markersize=10)

