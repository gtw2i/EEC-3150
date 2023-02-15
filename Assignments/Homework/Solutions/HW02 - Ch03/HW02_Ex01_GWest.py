x = input("binary: ")
n = len(x)

tot = 0
for i in range(n):
    print(int(x[i]))
    tot += int(x[i])*2**(n-i-1)
# end
print(tot)