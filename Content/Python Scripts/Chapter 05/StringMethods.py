x = 'tears in rain'

# split a string into a list on occurrences of the argument
y = x.split(' ')
print('split:', y)

# join a list of strings into one string with the
# calling string as the delimiter
z = 'abc'.join(y)
print('join:', z)

# remove beginning and trailing characters, defaults to whitespace
# NOTES:
# 1. returns new string, doesnt alter original
# 2. lstring and rstring remove leading and trailing whitespace, respectively
# 3. can accept an argument, will remove an combination of those characters
x = '      string     '
y = x.strip()
print("strip:", y)

x = 'xyxystring'
y = x.strip('xy')
print("strip:", y)

x = 'tears in rain'

# split a string into a list on occurrences of the argument
old = 'tears'
new = 'blood'
y = x.replace(old, new)
print('replace:', y)

# capitalization methods
y = x.upper()
print( 'upper:', y )
y = y.lower()
print( 'lower:', y )
y = y.title()
print( 'title:', y )
y = y.capitalize()
print( 'capitalize:', y )

# return first occurrence of input string
# functions like list.index
x = 'tears in rain'
n = x.find('in')
print( 'find:', n )

# find with search range
x = 'tears in rain in'
start = 10
end = 200
n = x.find('in', start, end)
print( 'find:', n )

# escape characters

# \n = new line
x = 'tears\nin\nrain'
print(x)
# \t = tab
x = 'tears\tin\train'
print(x)

# test letter types
x = 'bladeRUNNER2049'
for s in x:
    print( s, s.isdigit(), s.isalpha(),
          s.islower(), s.isupper(), s.istitle() )


