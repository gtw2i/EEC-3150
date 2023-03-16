import numpy as np
from matplotlib import pyplot as plt

nPts = 50

a = 0.1

x = np.linspace(0,1,nPts)
r = a*(2*np.random.rand(nPts)-1)
y = x + r

plt.plot(x,y)