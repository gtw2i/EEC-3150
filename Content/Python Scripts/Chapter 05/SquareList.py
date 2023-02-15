def SquareList(x):
    y = []
    for i in x:
        y.append(i**2)
    # end
    return y

x = [1,2,3]
y = SquareList(x)
print( y )