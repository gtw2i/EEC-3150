import numpy as np
from numpy import linalg as LA

# solve this system:
# 2x_0 -  x_1 = 4
# 3x_0 + 2x_1 = 1

A = np.array([[2,-1],[3,2]])
b = np.array([4,1])
print(A)
print(b)

# solving with solve
x = LA.solve(A,b)
print(x)

# check
print(np.matmul(A,x), "recovers b")

# solving with inv and matmul
Ainv = LA.inv(A)
x = np.matmul(Ainv,b)
print(x)

# check
print(np.matmul(A,x), "recovers b")