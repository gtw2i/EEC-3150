def exp(x):
    return 2.718**x

def sinh(x):
    return (exp(x)-exp(-x))/2

def cosh(x):
    return (exp(x)+exp(-x))/2

def tanh(x):
    return sinh(x)/cosh(x)

def TrigH(x):
    return sinh(x), cosh(x), tanh(x)

x = 10
s, c, t = TrigH(x)
print(s,c,t)