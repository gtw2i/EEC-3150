def add(x, y):
    
    if len(x) != len(y):
        raise ValueError("arguments of add() must have same length")
    
    sums = []
    
    for i,j in zip(x,y): 
        sums.append(i+j)
    # end
            
    return sums
# end

a = [1,2,3]
b = [1,2,3,4]

c = add(a,b)
print(c)