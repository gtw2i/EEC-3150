import numpy as np
from numpy import linalg as LA

# eye
I = np.eye(3)
print(I)
print()

# transpose
A = np.arange(4).reshape((2,2))
print(A)
print(A.T)
print()

# norm
v = np.arange(3,5)
print(v)
print(LA.norm(v))
print(LA.norm(v,1))
print(LA.norm(v,2))
print(LA.norm(v,np.inf))
print()

# matmul, dot, inner, outer
x = np.array([1,2,1])
y = np.array([2,-1,3])
print(x)
print(y)
print(np.matmul(x,y))
print(np.dot(x,y))
print(np.inner(x,y))
print(np.outer(x,y))
print()

A = np.array([[1,-1],[1,1]])
B = np.array([[1,-1],[1,2]])
print(A)
print(B)
print(np.matmul(A,B))
print(np.dot(A,B))
print()

# det
A = np.array([[1,-1],[1,1]])
B = np.array([[1,-1],[1,2]])
print(LA.det(A))
print(LA.det(B))
print()

# inv
A = np.array([[1,-1],[1,1]])
B = np.array([[1,-1],[1,2]])
print(LA.inv(A))
print(LA.inv(B))
Ainv = LA.inv(A)
print(np.matmul(A,Ainv))
print(np.matmul(Ainv,A))
print()

# eig
A = np.array([[1,-1],[-1,1]]) # symmetric
val, vec = LA.eig(A)
print(val)
print(vec)
print( np.matmul(A,vec[:,0])/vec[:,0], "equals the 0-th eigenvalue" )
print()

A = np.array([[1,-1],[1,1]]) # non-symmetric
val, vec = LA.eig(A)
print(val)
print(vec)
print()

# solve
# 2x_0 -  x_1 = 4
# 3x_0 + 2x_1 = 1
A = np.array([[2,-1],[3,2]])
b = np.array([4,1])
print(A)
print(b)
x = LA.solve(A,b)
print(x)
print(np.matmul(A,x), "recovers b")

# getting x manually with inv and matmul
Ainv = LA.inv(A)
x = np.matmul(Ainv,b)
print(x)
print(np.matmul(A,x), "recovers b")

