import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def CalcPi(n):
    x = np.random.uniform(-1,1,n)
    y = np.random.uniform(-1,1,n)
    
    m = 0.0
    for i in range(n):
        if x[i]**2 + y[i]**2 < 1:
            m+=1
        # end
    # end
    
    return 4*m/n
# end

arr = 2**np.arange(4,16,2)
print(arr)

nRep = 100

pis = []
for i in range(nRep):
    pis.append([])
    for j in arr:
        pis[i].append(CalcPi(j))
    # ene
# end
pis = np.array(pis)

print(pis.shape)
print(arr.shape)

df = pd.DataFrame(pis, columns=arr)


print(df)


df.boxplot()
