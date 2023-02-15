# Author: Jose Tovar
# Collaborators: Laura Cornelius
# Description: Rational(object) is an ADT used to work with rational numbers and get around the intrinsic innacuracies
# of binary representations of decimal numbers

class Rational(object):
    """Represents a rational number."""

    def __init__(self, numer, denom):
        """Constructor creates a number with the given numerator
        and denominator and reduces it to lowest terms."""
        self.numer = numer
        self.denom = denom
        self._reduce()

    def numerator(self):
        """Returns the numerator."""
        return self.numer

    def denominator(self):
        """Returns the denominator."""
        return self.denom

    def __str__(self):
        """Returns the string representation of the number."""
        return str(self.numer) + "/" + str(self.denom)

    def _reduce(self):
        """Helper to reduce the number to lowest terms."""
        divisor = self._gcd(abs(self.numer), self.denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor

    def _gcd(self, a, b):
        """Euclid's algorithm for greatest common divisor."""
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    # Methods for arithmetic and comparison operators
    def __add__(self, other):
        """Returns the sum of the numbers."""
        newNumer = self.numer * other.denom + \
                   other.numer * self.denom
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)

    def __sub__(self, other):
        """Returns the difference between the two numbers"""
        newNumer = self.numer * other.denom - \
                   other.numer * self.denom
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)

    def __mul__(self, other):
        """Returns the product of two numbers"""
        newNumer = self.numer * other.numer
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)

    def __truediv__(self, other):
        """Returns self / other"""
        newNumer = self.numer * other.denom
        newDenom = self.denom * other.numer
        return Rational(newNumer, newDenom)
        # 8   3

    def __mod__(self, other):
        # format is self % other
        x = other
        if self < other:
            modulo = self
        else:
            while x < self:
                x = x + other
            modulo = self - (x - other)
        return modulo

    def __lt__(self, other):
        """Returns self < other."""
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes < means

    def __le__(self, other):
        """Returns self <= other"""
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes <= means

    def __gt__(self, other):
        """Returns self>other"""
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes > means

    def __ge__(self, other):
        """Returns self < other."""
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes >= means

    def __eq__(self, other):
        """Tests self and other for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.numer == other.numer and \
                   self.denom == other.denom

    def __ne__(self, other):
        """Returns self != other"""
        if self is not other:
            return True
        elif type(self) != type(other):
            return True
        else:
            return self.numer != other.numer and self.denom != other.denom

    def __pow__(self, power, modulo=None):
        """Returns self ** power"""
        newNumer = self.numer ** power
        newDenom = self.denom ** power
        return Rational(newNumer, newDenom)
