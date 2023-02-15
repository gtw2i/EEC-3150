x = 4

if x%2 == 0:
    if x%3 == 0:
        print("x is divisible by 2 and 3")
    else:
        print("x is divisible by 2, not 3")
    # end
elif x%3 == 0:
    print("x is divisible by 3, not 2")
else:
    print("x isn’t divisible by 2 or 3")
# end

print("Done")
