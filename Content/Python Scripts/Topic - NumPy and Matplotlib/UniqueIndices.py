import numpy as np

x = np.random.randint(0,5,50)
print(x)

unq = np.unique(x)
print(unq)

ind = []
for i in unq:
    ind.append( list(np.where(x==i)[0]) )
    print(i,ind[i])
# end

print(x[ind[0]])

print(np.delete(x,ind[0]))