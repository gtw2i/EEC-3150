def GetFirstNPrimes(n):
    primes = [2]
    
    i = 3
    while len(primes) < n:
        isPrime = True
        for p in primes:
            if i%p == 0:
                isPrime = False
                break
            # end
        # end
        if isPrime:
            primes.append(i)
        # end
        i += 1
    # end
    
    return primes
# end

primes = GetFirstNPrimes(10)
print(primes)