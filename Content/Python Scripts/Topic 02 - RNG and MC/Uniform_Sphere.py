import matplotlib.pyplot as plt
import numpy as np

nPts = 12000

phi = np.random.uniform(0,2*np.pi,nPts)

# the naive, wrong way
#theta = np.random.uniform(0,np.pi,nPts)

# the correct way
theta = np.arccos(np.random.uniform(-1,1,nPts))

x = np.cos(phi)*np.sin(theta)
y = np.sin(phi)*np.sin(theta)
z = np.cos(theta)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x,y,z,s=3)