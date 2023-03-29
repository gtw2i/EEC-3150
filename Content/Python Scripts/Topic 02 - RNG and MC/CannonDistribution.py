import numpy as np
from matplotlib import pyplot as plt

def solve(y0, v0, theta):
    
    g = 9.8
    vy0 = v0*np.sin(theta)
    
    t1 = (-vy0 + (vy0**2 - 4*(-0.5*g)*y0)**0.5)/(-0.5*g)
    t2 = (-vy0 - (vy0**2 - 4*(-0.5*g)*y0)**0.5)/(-0.5*g)
    
    tf = max(t1,t2)
    
    xf = v0*np.cos(theta)*tf
    
    return xf, tf
# end


y0 = 1

v0 = 3
v0_err = 0.1

theta0 = np.radians(45)
theta0_err = np.radians(4)

nSamp = 10000

xs = np.zeros(nSamp)
ts = np.zeros(nSamp)

for i in range(nSamp):
    v = v0 + np.random.uniform(-v0_err,v0_err,1)[0]
    theta = theta0 + np.random.uniform(-theta0_err,theta0_err,1)[0]
    
    xf, tf = solve(y0,v,theta)
    xs[i] = xf
    ts[i] = tf
# end

# print(xs)

plt.hist(ts,bins=30)





