def dot1(x,y):
    n = len(x)
    
    total = 0
    for i in range(n):
        total += x[i]*y[i]
    # end
    return total
# end

def dot2(x,y):
    
    total = 0
    for i,j in zip(x,y):
        total += i*j
    # end
    return total
# end

x = [1,2,3]
y = [4,5,6]

print( dot1(x,y), dot2(x,y) )