import numpy as np
from matplotlib import pyplot as plt

mean = [0,0]
cov = np.array( [ [ 1, 0 ],
                  [ 0, 1 ] ] )

nPts = 10000
X = np.random.multivariate_normal(mean=mean,cov=cov,size=nPts)

fig = plt.figure(figsize=(6,6))
plt.plot(X[:,0],X[:,1],'.')
plt.xlim([-4,4])
plt.ylim([-4,4])

fig = plt.figure(figsize=(6,6))
plt.hist2d(X[:,0],X[:,1],bins=20)
plt.xlim([-4,4])
plt.ylim([-4,4])