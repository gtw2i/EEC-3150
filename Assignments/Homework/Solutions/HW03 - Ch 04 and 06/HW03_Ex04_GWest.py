def fact1(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans
# end

def Trig(x,n):
    s = 0
    c = 0
    for i in range(n):
        s += ((-1)**i)*(x**(2*i+1))/fact1(2*i+1)
        c += ((-1)**i)*(x**(2*i))/fact1(2*i)
    # end
    return s, c
# end

x = 3.14159
n = 10
print(Trig(x,n))