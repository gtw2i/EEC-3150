x = 0.1

n = 50
total = 0.0
binary = '0.'
for i in range(1,n):
    test = total + 2**(-i)
    if test < x:
        total = test
        binary +='1'
    else:
        binary += '0'
    # end
    print(x, test, binary)
# end

print()
print(x, total, binary, total == x)
        