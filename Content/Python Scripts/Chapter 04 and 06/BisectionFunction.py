def find_root(x, power, epsilon):
    
    # Find interval containing answer 
    if x < 0 and power%2 == 0:
        print("can't find even root of negative number")
        return None #Negative number has no even-powered roots 
    # end
    
    # define values
    low = min(-1, x) 
    high = max(1, x) 
    ans = (high + low)/2
    
    # Use bisection search 
    while abs(ans**power - x) >= epsilon: 
        if ans**power < x: 
            low = ans 
        else: 
            high = ans 
        # end
        ans = (high + low)/2 
    return ans 
# end

root1 = find_root(2, 2, 0.01)
print(root1)

root2 = find_root(100, 3, 0.01)
print(root2)