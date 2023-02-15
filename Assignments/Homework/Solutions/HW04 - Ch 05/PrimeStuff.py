def getPrimes(n):
    
    primes = [2]

    i = 3
    while True:
        if i > n:
            break
        # end
        isPrime = True
        for p in primes:
            if i%p == 0:
                i += 1
                isPrime = False
                break
            # end
        # end
        if isPrime:
            primes.append(i)
        # end
    # end
    
    return primes

# end

def getPrimeFactorization(n):
    fact = {}
    total = n
    primes = getPrimes(n)
    
    for p in primes:
        power = 0
        while total%p == 0:
            total /= p
            power += 1
        # end
        if power > 0:
            fact[p] = power
        # end
    # end
    return fact
# end

print( getPrimeFactorization(105) )







