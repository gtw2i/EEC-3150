def HMS(n):
    
    h = 0
    m = 0
    s = n
    
    while s >= 60:
        m += 1
        s -= 60
    # end
    
    while m >= 60:
        h += 1
        m -= 60
    # end
    
    string = str(h)+'h '+str(m)+'m '+str(s)+'s'
    
    print(string)
# end

HMS(360)