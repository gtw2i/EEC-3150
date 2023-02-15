def HarmRec(n):
    n = float(n)
    if n == 1.0:
        return 1.0
    elif n > 1.0:
        return 1.0/n + HarmRec(n-1)
    # end
# end

def HarmNon(n):
    total = 0
    for i in range(1,n+1):
        total += 1.0/i
    # end
    return total
# end

n = 10
for i in range(1,n+1):
    print(HarmRec(i),HarmNon(i))