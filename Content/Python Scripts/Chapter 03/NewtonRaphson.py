c = 2
eps = 0.01
ans = 100
print(c, ans**2)
i = 0
while abs(ans**2 - c) >= eps:
    ans = ans - (ans**2 - c)/(2*ans)
    i += 1
    print(c, ans**2)
# end
print(i)
print('sqrt(', c, ') is about', ans)