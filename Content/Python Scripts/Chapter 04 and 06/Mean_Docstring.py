def mean(*args):
    """
    This function returns
    the mean of the
    variable number of
    arguments (float or int)
    provided
    """
    
    tot = 0 
    for a in args: 
        print(a)
        tot += a 
    # end
    
    return tot/len(args) 
# end

help(mean)