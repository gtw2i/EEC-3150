def sumAtoB( A, B ):
    
    total = 0
    for i in range(A,B+1):
        total += i
    # end
    
    return total
# end

tot = sumAtoB( 1,10 )

print(tot)