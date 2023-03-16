def Mode(x):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    mode = x[0]
    for k,v in d.items():
        if v > d[mode]:
            mode = k
    
    return mode

x = [1,1,2,2,2,3,3,3,3,3]
m = Mode(x)
print(m)