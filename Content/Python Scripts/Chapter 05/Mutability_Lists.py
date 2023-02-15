x = [1]

y = x
print(y, x)
print( id(y), id(x) )

x = [1,2]
#x += [2]
#x.append(2)
print(y, x)
print( id(y), id(x) )