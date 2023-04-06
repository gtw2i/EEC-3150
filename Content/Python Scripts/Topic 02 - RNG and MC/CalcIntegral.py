import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

n = 10000

xmin = 0
xmax = 1

ymax = 1

x = np.random.uniform(xmin,xmax,n)
y = np.random.uniform(   0,ymax,n)

m = 0.0
for i in range(n):
    if f(x[i]) > y[i]:
        m+=1
    # end
# end

INT = ymax*(xmax-xmin)*m/n
print(INT)

plotX = np.linspace(xmin,xmax,100)
plotY = f(plotX)

fig = plt.figure(figsize=(10,10))

ind1 = f(x) >  y
ind2 = f(x) <= y

plt.plot(x[ind1],y[ind1],'r.',markersize=5)
plt.plot(x[ind2],y[ind2],'b.',markersize=5)

plt.plot(plotX,plotY,'k',linewidth=5)

