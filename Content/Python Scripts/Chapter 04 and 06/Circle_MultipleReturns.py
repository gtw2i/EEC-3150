def DiamPerim( r ):
    d  = 2*r        # diameter
    pi = 3.1415     # pi
    p  = pi*d       # perimeter
    return d, p
# end

radius = 10
d, p = DiamPerim( radius )

print(d,p)