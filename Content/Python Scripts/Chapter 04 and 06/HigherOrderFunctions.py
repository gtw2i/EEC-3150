def f(x):
    return x
def g(x):
    return -x
def abs2(x,F,G):
    if x>0:
        return F(x)
    else:
        return G(x)
    # end
# end

print(abs2(-1,f,g))