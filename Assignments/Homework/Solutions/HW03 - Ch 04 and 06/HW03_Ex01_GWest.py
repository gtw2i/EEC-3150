def Reverse(s):
    x = ''
    for i in range(len(s)):
        x += s[-i-1]
    # end
    return x
# end

s = 'string'
print( s )
print( Reverse(s) )