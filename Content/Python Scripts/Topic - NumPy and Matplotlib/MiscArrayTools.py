import numpy as np

# reshape
print("reshpae")
x = np.arange(0,10)
print(x)
print(np.reshape(x,(5,2)))
print(np.reshape(x,(2,5)))
print()

x = np.random.rand(4,4)
print(x)
print(np.reshape(x,(8,2)))
print(np.reshape(x,(4,2,2)))
print()

# flatten
print("flatten")
x = np.random.rand(4,4)
print(x)
print(x.flatten())
print()

# flipud, fliplr, rot09
print("flip, rot")
x = np.reshape(np.arange(0,10),(5,2))
print(x)
print(np.flipud(x))
print(np.fliplr(x))
print(np.rot90(x,1))
print(np.rot90(x,2))
print()

# roll
print("roll")
x = np.arange(0,10)
print(x)
print(np.roll(x,1))
print(np.roll(x,-2))
print()

# sort, argsort
print("sort")
x = np.random.rand(10)
print(x)
print(np.sort(x))
ind = np.argsort(x)
print(ind)
print(x[ind])
print()

# sort with axis
x = np.reshape(np.random.randint(0,9,9),(3,3))
print(x)
print(np.sort(x))
print(np.sort(x,axis=0))
print(np.sort(x,axis=1))
print()

# transpose
print("transpose")
x = np.reshape(np.arange(0,9),(3,3))
print(x)
print(x.T)
print()

# unique
print("unique")
x = np.random.randint(0,5,10)
print(x)
print(np.unique(x))
print()

# append, insert, delete
print("append, insert, delete")
x = np.arange(0,10)
print(x)
print(np.append(x,-1))
print(np.insert(x,0,-1))
print(np.delete(x,0))




