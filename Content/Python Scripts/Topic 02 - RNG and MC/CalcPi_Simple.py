import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


n = 10000

x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)

m = 0.0
for i in range(n):
    if x[i]**2 + y[i]**2 < 1:
        m+=1
    # end
# end

pi = 4*m/n

print(np.pi)
print(pi)