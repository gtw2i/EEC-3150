import numpy as np
from matplotlib import pyplot as plt

nPts = 1000

m = 1
b = 0

std = 0.1

x = np.linspace(0,1,nPts)
y = m*x + b + np.random.normal(0,std,nPts)

plt.plot(x,y,'.')

print(np.var(x))
print(np.var(y))
print(np.cov(x,y))
print(np.corrcoef(x,y))
print(np.corrcoef(x,y)[0,1])
