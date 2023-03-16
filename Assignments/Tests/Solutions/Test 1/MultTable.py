def MultTable(n):
    d = {}
    for i in range(1,n+1):
        d[i] = {}
    # end
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = i*j
    
    return d
# end

d = MultTable(10)
print(d[3][4])