x = 42

epsilon = 0.01 
low = 0
high = max(1, x) 
ans = (high + low)/2 

i = 0
while abs(10**ans - x) >= epsilon:
    #print(low,high)
    
    if 10**ans < x: 
        low = ans 
    else:
        high = ans 
    # end
    
    ans = (high + low)/2
    i += 1
# end
#print(i)
print('log(',x,') is approx.', ans) 
print('check: 10**',ans,'= ', 10**ans) 