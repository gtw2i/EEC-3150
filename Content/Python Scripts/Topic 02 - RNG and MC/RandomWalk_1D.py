import numpy as np
import matplotlib.pyplot as plt

nPts = 100

x = np.zeros(nPts)

for i in range(nPts-1):
    
    # uniform
    #r = np.random.uniform(-1,1,1)[0]
    
    # normal
    #r = np.random.normal(0,1,1)[0]
    
    # normal with drift
    #r = np.random.normal(30.0/nPts,1,1)[0]
    
    # discrete
    r = np.random.choice([-1,1],1)[0]
    
    x[i+1] = x[i] + r
# end

plt.plot(x)
plt.ylim(-35,35)
