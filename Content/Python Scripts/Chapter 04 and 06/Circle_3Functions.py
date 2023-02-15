def diameter( r ):
    return 2*r
# end

def perimeter( r ):
    pi = 3.1415
    return 2*pi*r
# end

def area( r ):
    pi = 3.1415
    return pi*r**2
# end

radius = 10

d = diameter( radius )
p = perimeter( radius )
a = area( radius )

print(d,p,a)