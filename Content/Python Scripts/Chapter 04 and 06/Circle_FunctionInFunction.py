def diameter( r ):
    return 2*r
# end

def perimeter( r ):
    pi = 3.1415
    d = diameter( r )
    return pi*d
# end

r = 10
p = perimeter( r ) 
print( p )