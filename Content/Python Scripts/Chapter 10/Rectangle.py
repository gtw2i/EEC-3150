class Rectangle:
    def __init__(self, L, W):
        self._length = L
        self._width  = W
    def get_area(self):
        return self._length*self._width
    def get_perimeter(self):
        return 2*(self._length+self._width)

r = Rectangle(4,5)
print(r.get_area(), r.get_perimeter())