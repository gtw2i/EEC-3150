x = 100

epsilon = 0.01 
low = 0
high = max(1, x) 
ans = (high + low)/2 

i = 0
while abs(ans**2 - x) >= epsilon:
    print(low,high)
    
    if ans**2 < x: 
        low = ans 
    else:
        high = ans 
    # end
    
    ans = (high + low)/2
    i += 1
# end
print(i)
print('sqrt(',x,') is approx.', ans) 
print( ans**2, x)