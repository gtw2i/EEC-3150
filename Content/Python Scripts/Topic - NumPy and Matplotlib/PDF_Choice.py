import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return np.sin(np.pi*x)

def PDF(f,x):
    y = f(x)
    y /= sum(y)
    return y

nSamp = 10000

nRes = 10
xLim = (0,1)

grid = np.linspace(xLim[0],xLim[1],nRes)
prob = PDF(f,grid)
samples = np.random.choice(grid,nSamp,p=prob)

plt.hist(samples,bins=50)


