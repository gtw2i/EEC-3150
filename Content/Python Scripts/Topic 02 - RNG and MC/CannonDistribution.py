import numpy as np
from matplotlib import pyplot as plt

def solve(yi, vi, theta):
    
    g = 9.8
    vyi = vi*np.sin(theta)
    
    t1 = (-vyi + (vyi**2 - 4*(-0.5*g)*yi)**0.5)/(-0.5*g)
    t2 = (-vyi - (vyi**2 - 4*(-0.5*g)*yi)**0.5)/(-0.5*g)
    
    tf = max(t1,t2)
    
    xf = vi*np.cos(theta)*tf
    
    return xf, tf
# end


yi = 1

vi = 3
vi_err = 0.1

theta = np.radians(45)
theta_err = np.radians(4)

nSamp = 10000

xs = np.zeros(nSamp)
ts = np.zeros(nSamp)

for i in range(nSamp):
    v = vi + np.random.uniform(-vi_err,vi_err,1)[0]
    theta2 = theta + np.random.uniform(-theta_err,theta_err,1)[0]
    
    xf, tf = solve(yi,v,theta2)
    xs[i] = xf
    ts[i] = tf
# end

# print(xs)

plt.hist(ts,bins=30)





