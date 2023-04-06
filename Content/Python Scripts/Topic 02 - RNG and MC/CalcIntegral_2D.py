import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('dark_background')

def f(x,y):
    return np.exp(-(x**2+y**2))
# end

def SampleCylinder(nSamp,center,radius,height):
    theta = np.random.uniform(0,2*np.pi,nSamp)
    r     = radius*np.random.uniform(0,1,nSamp)**0.5
    
    x = r*np.cos(theta) + center[0]
    y = r*np.sin(theta) + center[1]
    z = np.random.uniform(0,height,nSamp)
    
    return x,y,z
# end

def CreateMesh(nRes,center,radius):
    xmin = center[0]-radius
    xmax = center[0]+radius
    ymin = center[1]-radius
    ymax = center[1]+radius
    
    x = np.linspace(xmin,xmax,nRes)
    y = np.linspace(ymin,ymax,nRes)
    
    X, Y = np.meshgrid(x,y)
    
    return X, Y
# end


nSamp = 2000
r = 3
h = 1
center = [0,0]

x, y, z = SampleCylinder(nSamp,center,r,h)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()

ax.scatter(x,y,z,s=2,c='r')

nUC = 0
inds = []
for i in range(nSamp):
    if f(x[i],y[i]) > z[i]:
        nUC += 1
        inds.append(i)
    # end
# end

Vcyl = np.pi*r**2*h

ans = Vcyl*nUC/nSamp
print(ans)
    
ax.scatter(x[inds],y[inds],z[inds],s=10,c='k')

nRes = 100
X, Y = CreateMesh(nRes,center,r)
Z = f(X,Y)

ax.plot_wireframe(X,Y,Z, rstride=10, cstride=10)



