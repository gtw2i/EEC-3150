n = int(input("give me a number: "))

i = 2
while True:
    if int(n/i) == n/i:
        print(n, "is not prime")
        break
    else:
        i += 1
    # end
    if i == n:
        print(n, "is prime")
        break
    # end