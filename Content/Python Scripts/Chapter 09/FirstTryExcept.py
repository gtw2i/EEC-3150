x = list(range(4))
#x = list(range(20))
print(x)

try:
    # try to get the 10th element
    y = x[10]
except:
    # else get the last element
    y = x[-1]
# end

print(y)