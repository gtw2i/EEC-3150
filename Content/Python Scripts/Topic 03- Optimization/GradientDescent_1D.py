import matplotlib.pyplot as plt
import numpy as np

def f(x):
    #return x**2
    #return x**4 - 4*x**3 - 12*x**2 + 16*x + 5
    return ( (x-1)**2+0.15 )*( (x+1)**2 )

def df(x):
    #return 2*x
    #return 4*x**3 - 12*x**2 - 24*x + 16
    return 2*(x - 1)*((x + 1)**2) + ((x - 1)**2 + 0.15)*(2*(x + 1))

def GD(df,start,rate,nStep):
    
    points = np.zeros(nStep)
    points[0] = start
    for i in range(nStep-1):
         points[i+1] = points[i] - rate*df(points[i])
    # end
    
    return points
# end

nStep = 25
start = 1.5
rate = 0.3

points = GD(df,start,rate,nStep)
graphX = np.linspace(-start*1.15,start*1.15,100)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

axes[0].plot(points,f(points))
axes[0].plot(graphX,f(graphX),'r--')

axes[1].plot(f(points))
