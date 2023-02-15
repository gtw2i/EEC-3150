x=1000
epsilon=0.01
step=epsilon**2
numGuesses=0
ans=0.0
while abs(ans**2-x) >= epsilon and ans*ans <= x:
    #print('step=',step,'ans=',ans)
    ans+=step
    numGuesses+=1
print('numGuesses =', numGuesses)
print('Answer',ans)