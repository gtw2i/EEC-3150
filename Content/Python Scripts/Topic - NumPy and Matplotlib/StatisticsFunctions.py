import numpy as np

# mean, average, median
x = np.random.randn(100)
print(np.average(x))
print(np.mean(x))
print(np.median(x))
print(np.average(x,weights=np.arange(100)**3))
print()

# std, var
print(np.std(x))
print(np.var(x))
print()

# cov, corrcoef
x = np.random.randn(100)
y = np.random.randn(100)
print(np.cov(x,y))
print(np.corrcoef(x,y))
print(np.corrcoef(x,y)[0,1])

X = np.random.randn(3,100)
print(np.cov(X))
print(np.corrcoef(X))
print()

# histogram
x = np.random.randn(10000)
bins, edges = np.histogram(x)
print(bins)
print(edges)

numBins = 20
low  = -5
high = 5
bins, edges = np.histogram( x, bins=numBins, range=(low,high))
print(bins)
print(edges)
print()

# histogram2d
x = np.random.randn(10000)
y = np.random.randn(10000)
bins, xedges, yedges = np.histogram2d(x,y)
print(bins)
print(xedges)
print(yedges)
print()

# bincount
x = np.random.randint(0,5,100)
print(np.bincount(x))







