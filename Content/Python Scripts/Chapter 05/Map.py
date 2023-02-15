def square(n):
    return n**2

x = [1,2,3]
y = list(map(square,x))
print(y)

# cast to string
z = list(map(str,x))
print(z)