x = [1]
print(x)

# append an element to the end of a list
x.append(2)
print("append:", x)

# append an iterable to the end of a list
x.extend([3])
print("extend:", x)
x.extend((1,))
print("extend:", x)

# insert an element at a specified index
x.insert(1,'a')
print("insert:", x)

# remove the first occurrence of the item in the list
x.remove(1)
print("remove:", x)

# remove the element at the index and return it, default is last element
y = x.pop(0)
print("pop:", x, y)
y = x.pop()
print("pop:", x, y)

# remove all elements
x.clear()
print("clear:", x)

x = [1,2,3,1,2,3,1]
print(x)

# return index of first occurrence of argument
n = x.index(1)
print("index:", n)

# two optional arguments, start and end of search range
start = 1
end   = 4
n = x.index(1,start)
print("index:", n)

n = x.index(1,start,end)
print("index:", n)

# count occurrences of argument
n = x.count(3)
print("count:", n)

# sort ascending
x.sort()
print("sort:", x)

# sort descending
x.sort(reverse=True)
print("sort:", x)

# reverse order
x.reverse()
print("reverse:", x)

# copy the list without worrying about mutability issues
y = x.copy()
x.append('a')
x = [1]
print("copy:", y, x)



