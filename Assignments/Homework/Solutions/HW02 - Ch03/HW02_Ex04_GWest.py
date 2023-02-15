x = 42
eps = 0.01
ans = 3

log10 = 2.3025

i = 0
while abs(10**ans - x) >= eps:
    ans = ans - (10**ans - x)/(log10*10**ans)
    i += 1
    print(x, 10**ans)
# end

#print(i)
print('log(',x,') is approx.', ans) 
print('check: 10**',ans,'= ', 10**ans) 