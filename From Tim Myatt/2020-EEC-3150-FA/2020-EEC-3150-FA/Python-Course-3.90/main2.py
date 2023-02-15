def power(x, y):
    """ Raise an integer x to an integer power y """
    if type(x) != int or type(y) != int:
        raise TypeError
    if x < 0 or y < 0:
        raise ValueError
    if y == 0:
        return 1
    else:
        p = x * power(x, y-1)
    return p

def factorial(n):
    """ Find x factorial """
    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError
    if (n == 1) or (n == 0):
        return 1
    else:
        return n * factorial(n-1)

def main():
    """ Taylor Series expansion of e^x """
    x = 5       # set the value for x (e^x)
    n = 500     # set the value for n (iterations)

    e_to_x = 1.0
    for i in range(1,n):
        try:
            e_to_x += (power(x,i) / factorial(i))
        except TypeError:
            print ("ERROR: Only integer types")
            break
        except ValueError:
            print ("ERROR: Only integers >= 0")
            break
    print(e_to_x)

if __name__ == '__main__':
    main()
