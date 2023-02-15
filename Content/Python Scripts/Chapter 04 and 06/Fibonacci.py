def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        f0 = 0
        f1 = 1
        for i in range(n-1):
            tmp = f1 + f0
            #print(f0, f1, tmp)
            f0 = f1
            f1 = tmp
        # end
        return f1
    # end
# end

def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib2(n-1) + fib2(n-2)
    # end
# end

for i in range(10):
    print(fib1(i),fib2(i))