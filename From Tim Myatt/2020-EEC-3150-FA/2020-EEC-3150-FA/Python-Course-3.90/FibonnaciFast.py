def fastFib(n, memo = None):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if memo == None:
        memo = {}
    if n == 0:
        return 0
    if n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

print(fastFib(41))