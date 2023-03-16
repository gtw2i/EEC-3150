import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,4*np.pi,1000)
s = np.sin(x)

ind = np.where(s>=0)

plt.plot(x[ind],s[ind])