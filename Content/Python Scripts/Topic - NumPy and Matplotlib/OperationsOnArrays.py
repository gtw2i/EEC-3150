import numpy as np

nPts = 3

# create two arrays
x = np.linspace(1,3,nPts)
print(x)
y = np.full(nPts,3)
print(y)
print()

# we can perform basic operations with scalars
print( x+10 )
print( x-10 )
print( x*10 )
print( x/10 )
print( 10/x )
print( x**10 )
print( -x )
print()

# we can perform element-wise operations between two arrays
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print()

# math functions
print(np.sin(x))
print(np.exp(y))
print()

# adding arrays of different sizes

# this will add r or c to each row or column of x2D
x2D = np.ones((3,3))
r = np.ones((1,3))
c = np.ones((3,1))
print( x2D )
print( r )
print( x2D+r )
print( c )
print( x2D+c )
print()

# adding this row and column makes a 5x5 array
print( np.ones((5,1))+np.ones((1,5)) ) 
print()

# convert 1D array into a row or column
x = np.arange(0,3)
print(x)
print(x[:,np.newaxis])
print(x[np.newaxis,:])

