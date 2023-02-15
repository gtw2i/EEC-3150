x=1000
epsilon=0.01

def findSqrt(x,epsilon):
    ans=x/2.0
    numGuesses=0
    while abs(ans**2-x) >= epsilon:
        #print('ans=',ans)
        numGuesses+=1
        ans = ans - (((ans**2) - x)/(2*ans))
    return ans, numGuesses

print('Answer=',findSqrt(x,epsilon))