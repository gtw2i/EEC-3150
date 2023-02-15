def ConcatStrings(x):
    y = x[0]
    for s in x[1:]:
        y += ' '
        y += s
    # end
    return y

x = ['who', 'am', 'i?']
y = ConcatStrings(x)
print( y )