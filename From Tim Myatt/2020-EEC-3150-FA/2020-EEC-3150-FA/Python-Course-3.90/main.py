class e_TO_x(object):
    """ An object raising e to the x power with n iterations"""
    def __init__(self):
        self.result = 0.0

    def __str__(self):
        return(str(self.result))

    def power(self, x, y):
        """ Raise an integer x to an integer power y """
        if type(x) != int or type(y) != int:
            raise TypeError
        if x < 0 or y < 0:
            raise ValueError
        if y == 0:
            return 1
        else:
            p = x * self.power(x, y-1)
        return p

    def factorial(self, n):
        """ Find x factorial """
        if type(n) != int:
            raise TypeError
        if n < 0:
            raise ValueError
        if (n == 1) or (n == 0):
            return 1
        else:
            return n * self.factorial(n-1)

    def calculate(self, x, n):
        """ Calculate the Taylor Series approximation of e^x """
        self.result = 1.0;
        for i in range(1,n):
            self.result += (self.power(x,i) / self.factorial(i))
        return self.result

def main():
    """ Taylor Series expansion of e^x """
    x = 5       # set the value for x (e^x)
    n = 500     # set the value for n (iterations)

    try:
        e_to_x = e_TO_x()
        e_to_x.calculate(x,n)
    except TypeError:
        print("ERROR: Only integer types")
    except ValueError:
        print("ERROR: Only integers >= 0")
    print(e_to_x)

if __name__ == '__main__':
    main()
