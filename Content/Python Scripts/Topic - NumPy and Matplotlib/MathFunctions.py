import numpy as np

# complex
x = 1+1j
print(x, np.conj(x))
print(x.real, x.imag, np.degrees(np.angle(x)))
print()

# min, max
x = np.arange(0,10).reshape((5,2))
print(x)
print(np.amin(x))
print(np.amin(x,axis=0))
print(np.amin(x,axis=1))
print(np.amax(x))
print(np.amax(x,axis=0))
print(np.amax(x,axis=1))
print()

# sum, prod
x = np.array([1,2,3,4])
print(np.sum(x))
print(np.cumsum(x))
print(np.prod(x))
print(np.cumprod(x))
print()







