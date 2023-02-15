x       = 2     # approx. the sqrt of this number

epsilon = 0.01  # precision
step    = 0.001 # step size to increment ans
ans     = 0.0   # guess at solution, initially 0.0

i = 0
# increment ans by step until a root is found or we know we can't find it
while abs(ans**2 - x) >= epsilon and ans**2 <= x:
    # increment and by step
    ans += step
    i += 1
# end

print(i)
# check whether a solution was found and print accordingly
if abs(ans**2 - x) >= epsilon: 
    print('Failed on square root of', x) 
else: 
    print('sqrt(',x,') is approx.', ans) 
# end