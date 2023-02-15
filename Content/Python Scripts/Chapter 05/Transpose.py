def Transpose(M):
    n = len(M)
    
    T = []
    for i in range(n):
        T.append([])
        for j in range(n):
            T[i].append(0)
    
    for i in range(n):
        for j in range(n):
            T[i][j] = M[j][i]
    
    return T
# end

M = [[1,2,3],[4,5,6],[7,8,9]]
T = Transpose(M)

for i in range(len(M)):
    print(M[i],T[i])