x = [1,2,3]

y = x
#y = x.copy()

assert id(x) != id(y), 'lists have same id'