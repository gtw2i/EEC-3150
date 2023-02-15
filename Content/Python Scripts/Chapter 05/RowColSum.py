def RowColSum(x):
    row = []
    for y in x:
        row.append(sum(y))
    # end
    
    n = len(x)
    m = len(x[0])
    col = []
    for i in range(n):
        col.append(0)
        for j in range(m):
            col[i] += x[j][i]
        # end
    # end
    
    return row, col
# end

x = [[1,2],[3,4]]
r, c =RowColSum(x)
for y in x:
    print(y)
# end
print()
print('row sum:', r)
print('col sum:', c)