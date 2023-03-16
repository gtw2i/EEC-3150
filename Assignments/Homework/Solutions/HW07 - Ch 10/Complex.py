class Complex:
    
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __str__(self):
        if self.r != 0:
            if self.i > 0:
                return f"{self.r}+{self.i}i"
            elif self.i<0:
                return f"{self.r}{self.i}i"
            else:
                return f"{self.r}"
        else:
            if self.i != 0:
                return f"{self.i}i"
            else:
                return "0"
        # end
    
    def __add__(self, other):
        return Complex(self.r+other.r, self.i+other.i)
    
    def __sub__(self, other):
        return Complex(self.r-other.r, self.i-other.i)
    
    def __mul__(self, other):
        a = self.r
        b = self.i
        c = other.r
        d = other.i
        R = (a*c-b*d)
        I = (a*d+b*c)
        return Complex(R,I)
    
    def __truediv__(self, other):
        a = self.r
        b = self.i
        c = other.r
        d = other.i
        R = (a*c+b*d)/(c*c+d*d)
        I = (b*c-a*d)/(c*c+d*d)
        return Complex(R,I)
    
    def __neg__(self):
        return Complex(-self.r,-self.i)
    
    def __eq__(self, other):
        if self.r==other.r and self.i==other.i:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if self.r!=other.r or self.i!=other.i:
            return True
        else:
            return False
    
# end

for i in [-1,0,1]:
    for j in [-1,0,1]:
        print( Complex(i,j) )

print()

a = Complex(1,1)
b = Complex(0,1)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(-a)
print(a==a)
print(a==b)
print(a!=a)
print(a!=b)


