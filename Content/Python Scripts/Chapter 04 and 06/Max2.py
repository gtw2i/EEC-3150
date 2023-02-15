def max2(*args):
    
    high = float('-inf')
    for a in args: 
        if a > high:
            high = a
        # end
    # end
    
    return high
# end

print(max2(-20000000000,-10000000000000))