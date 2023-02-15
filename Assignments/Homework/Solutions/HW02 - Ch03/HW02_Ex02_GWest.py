x       = 42

epsilon = 0.01
step    = 0.0001
ans     = 0.0

i = 0
while abs(10**ans - x) >= epsilon and 10**ans <= x:
    ans += step
    i += 1
    #print(10**ans, x)
# end
#print(i)
if abs(10**ans - x) >= epsilon: 
    print("FAILURE") 
else: 
    print('log(',x,') is approx.', ans) 
    print('check: 10**',ans,'= ', 10**ans) 
# end