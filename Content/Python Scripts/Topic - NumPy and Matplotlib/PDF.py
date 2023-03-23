import numpy as np
from matplotlib import pyplot as plt

def f(x):
    #return np.sin(np.pi*x)
    #return np.ones(x.shape)
    return x+0

def PDF( func, nSamp, xLim, nRes ):
    
    grid = np.linspace(xLim[0],xLim[1],nRes+1)
    grid = grid[:-1]
    dx = grid[1]-grid[0]
    
    prob = func(grid)
    prob = prob/np.sum(prob)
    prob = np.cumsum(prob)
    
    r = np.random.uniform(0,1,nSamp)
    r2 = np.random.uniform(0,dx,nSamp)
    
    samples = []
    for i in range(nSamp):
        ind = 0
        while True:
            if r[i] <= prob[ind]:# or ind==nRes-1:
                break
            else:
                ind += 1
            # end
        # end
        
        val = grid[ind] + r2[i]
        #val *= max(grid)/(max(grid)+dx)
        
        samples.append(val)
    # end
    
    return samples, r
# end

nSamp = 10000

nRes = 30
xLim = (0,1)

samples, r = PDF(f,nSamp,xLim,nRes)

plt.hist(samples,bins=nRes*2)






