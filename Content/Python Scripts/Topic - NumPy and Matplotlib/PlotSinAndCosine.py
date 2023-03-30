import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,2*np.pi,50)
s = np.sin(x)
c = np.cos(x)

plt.plot(x,s,'b.',markersize=2)
plt.plot(x,c,'g--',linewidth=2)