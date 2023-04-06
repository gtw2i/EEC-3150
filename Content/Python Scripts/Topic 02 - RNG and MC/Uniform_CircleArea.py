import numpy as np
import matplotlib.pyplot as plt

nPts = 3000

theta = np.random.uniform(0,2*np.pi,nPts)
r = np.random.uniform(0,1,nPts)**0.5    # note the sqrt

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y,'.',markersize=3)

plt.xlim(-1,1)
plt.ylim(-1,1)