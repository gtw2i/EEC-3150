import numpy as np
import matplotlib.pyplot as plt

nPts = 100

theta = np.random.uniform(0,2*np.pi,nPts)
x = np.cos(theta)
y = np.sin(theta)

plt.plot(x,y,'.',markersize=3)

plt.xlim(-2,2)
plt.ylim(-2,2)