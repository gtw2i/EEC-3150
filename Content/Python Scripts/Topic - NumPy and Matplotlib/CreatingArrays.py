import numpy as np

# createa list
x = [1,2,3,4.0]
print(x)

# convert to array
y = np.array(x)
print(y)

# force an integer data type
y = np.array(x, dtype=np.int32)
print(y)
print(y.shape)

# create 2d list
x = [[1,2],[3,4]]
print(x)

# convert to array
y = np.array(x)
print(y)
print(y.shape)

# other array creation methods
print( np.zeros(10) )
print( np.zeros((5,2)) )
print( np.ones(10) )
print( np.ones((5,2)) )
print( np.eye(3) )
print( np.full(3,2) )
print( np.full((3,3),2) )
print( np.arange(0,10) )
print( np.arange(0,10,2) )
print( np.arange(0,10,0.1) )
print( np.linspace(0,1,11) )
print( np.random.rand(10) )
print( np.random.rand(3,4) )

