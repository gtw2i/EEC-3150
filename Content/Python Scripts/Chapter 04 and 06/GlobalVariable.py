def f():
    global x
    x += 1
# end

x = 1
print(x)
f()
print(x)