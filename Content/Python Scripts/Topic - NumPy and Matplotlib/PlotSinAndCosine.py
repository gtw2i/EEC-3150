import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,2*np.pi,100)
s = np.sin(x)
c = np.cos(x)

plt.plot(x,s)
plt.plot(x,c)