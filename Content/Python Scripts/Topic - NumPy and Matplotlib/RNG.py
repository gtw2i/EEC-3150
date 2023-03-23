import numpy as np

# set seed
np.random.seed(0)

# rand, randn, randint
x = np.random.rand(10)
print(x)
x = np.random.rand(10,2)
print(x)
x = np.random.randn(10,2)
print(x)
x = np.random.randint(0,10,10)
print(x)
print()

# uniform
x = np.random.uniform(0,10,10)
print(x)
x = np.random.uniform(0,10,(10,2))
print(x)
print()

# normal
x = np.random.normal(0,1,10) # mean = 0, std = 1
print(x)
print()

mean = [0,0]
cov = np.diag([1,2])

x = np.random.multivariate_normal(mean=mean,cov=cov,size=10) # mean = 0, std = 1
print(x)
print()

# shuffle, permutation
x = np.arange(0,10)
print(x)
x = np.random.permutation(x)
print(x)
np.random.shuffle(x)
print(x)
print()

# choice
x = np.arange(0,4)
print(x)

nPts = 10
samples = np.random.choice(x,nPts)
print(samples)

weights = [ 0.7, 0.1, 0.1, 0.1 ]
samples = np.random.choice(x,nPts,p=weights)
print(samples)




