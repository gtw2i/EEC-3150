import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,2*np.pi,100)
s = np.sin(x)
c = np.cos(x)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6,3))
axes[0].plot(x,s)
axes[1].plot(x,c)

# individual axis titles
axes[0].set_title('sin')
axes[1].set_title('cos')

# full figure title
fig.suptitle('plot')

# better axis spacing
plt.tight_layout()