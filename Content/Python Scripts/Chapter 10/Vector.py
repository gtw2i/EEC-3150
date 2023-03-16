class Vector:
    
    def __init__(self, comp):
        if all( [isinstance(x, (int,float)) for x in comp] ):
            self.comp = comp
            self.dim = len(comp)
        else:
            raise ValueError("Vectors should only have numeric types")
        
    def __str__(self):
        return str(self.comp)
    
    def __getitem__(self,key):
        return self.comp[key]
    
    def __add__(self, other):
        if len(self.comp) != len(other.comp):
            raise ValueError("Vectors must be of same length.")
        return Vector([x + y for x, y in zip(self.comp, other.comp)])
    
    def __sub__(self, other):
        if len(self.comp) != len(other.comp):
            raise ValueError("Vectors must be of same length.")
        return Vector([x - y for x, y in zip(self.comp, other.comp)])
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector([x * scalar for x in self.comp])
        else:
            raise TypeError("Multiplication not defined for these types.")
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector([ x / scalar for x in self.comp])
        else:
            raise TypeError("Multiplication not defined for these types.")

    def __neg__(self):
        return Vector([ -x for x in self.comp])
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return all( [ i==j for i,j in zip(self.comp,other.comp) ] )
        else:
            raise TypeError("Operands must be Vectors")
    
    def __ne__(self, other):
        if isinstance(other, Vector):
            return all( [ i!=j for i,j in zip(self.comp,other.comp) ] )
        else:
            raise TypeError("Operands must be Vectors")

v1 = Vector([1,2])
v2 = Vector([3,4])
print(v1)
print(v1[0])
print(v1+v2)
print(v1-v2)
print(v1*2)
print(2*v1)
print(v1/2)
print(-v1)
print(v1==v1)
print(v1==v2)
print(v1!=v2)

