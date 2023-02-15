def Split(s,n):
    a = s[:n]
    b = s[n:]
    return a,b
# end

print(Split('abcd',2))