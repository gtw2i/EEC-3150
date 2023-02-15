def CharCount(string):
    
    d = {}
    for s in string:
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
        # end
    # end
    return d
# end

def WordCount(string):
    
    d = {}
    for s1 in string.split():
        s = s1.lower().strip(' ,.')
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
        # end
    # end
    return d
# end

def PrintSortedDict(d):
    k = list(d.keys())
    v = list(d.values())
    
    n = len(k)
    while n > 0:
        maxInd = 0
        for i in range(n):
            if v[i] > v[maxInd]:
                maxInd = i
            # end
        # end
        print(k[maxInd],v[maxInd])
        k.pop(maxInd)
        v.pop(maxInd)
        n = len(k)
    # end
# end

s = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."

c = CharCount(s)
print(c)

w = WordCount(s)
print(w)

PrintSortedDict(c)



