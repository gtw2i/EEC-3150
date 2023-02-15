def ConcatStrings(*x):
    s = ''
    for i in x:
        s += i
    # end
    return s
# end

print(ConcatStrings('tears','in','rain'))