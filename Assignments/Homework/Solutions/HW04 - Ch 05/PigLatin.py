def PL(s):
    vowels = 'aeiou'
    s = s.lower()
    
    i = 0
    while s[i] not in vowels:
        i += 1
    # end
    
    a = s[:i]
    b = s[i:]
    
    x = b+a+'ay'
    return x
# end

def PigLatin(s):
    x = s.split(' ')
    n = len(x)
    for i in range(n):
        x[i] = PL(x[i])
    # end
    s = ' '.join(x)
    return s
# end


s = 'tears in rain'
print(PigLatin(s))