x = [1,2,3]
#x = list(range(20))
print(x)

try:
    # try to get the 10th element
    y = x[10]
except:
    # else get the last element
    print("list index out of range, returning last element")
    y = x[-1]
# end

print(y)