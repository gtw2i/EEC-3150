def mean(*args):
    
    print(args)
    print(type(args))
    
    tot = 0 
    for a in args: 
        print(a)
        tot += a 
    # end
    
    return tot/len(args) 
# end

print(mean(1,2,3))