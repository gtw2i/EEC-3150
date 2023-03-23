import numpy as np
from numpy import linalg as LA
from matplotlib import pyplot as plt

nPts = 1000

m = 1
b = 0

std = 0.2

x = np.linspace(-1,1,nPts)
y = m*x + b + np.random.normal(0,std,nPts)

fig = plt.figure(figsize=(6,6))
plt.plot(x,y,'.')
plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])

R = np.corrcoef(x,y)

w, v = LA.eig(R)
print(w)
print(v)

v2 = v.copy()

v2[:,0] *= w[0]**0.5
v2[:,1] *= w[1]**0.5

plt.plot([0,v2[0,0]],[0,v2[1,0]],'r')
plt.plot([0,v2[0,1]],[0,v2[1,1]],'r')





