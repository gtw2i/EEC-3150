import numpy as np
import matplotlib.pyplot as plt

nPts = 100

X = np.zeros((nPts,2))

for i in range(nPts-1):
    
    # uniform
    # r = np.random.uniform(-1,1,2)
    
    # normal
    # r = np.random.normal(0,1,2)
    
    # normal with drift
    # mean = np.ones(2)*10/nPts
    # cov  = np.eye(2)*0.3
    # r = np.random.multivariate_normal(mean=mean,cov=cov,size=1)[0]
    
    # discrete
    N = [0,1]
    S = [0,-1]
    E = [-1,0]
    W = [1,0]
    direction = [N,S,E,W]
    ind = np.random.choice(range(4),1)[0]
    r = direction[ind]
    
    X[i+1,:] = X[i,:] + r
# end

plt.plot(X[:,0],X[:,1],linewidth=1)
plt.xlim(-15,15)
plt.ylim(-15,15)
