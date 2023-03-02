class Person:
    
    def __init__(self, name):
        self._name = name

p = Person("Graham")

print(p._name)

p._name = 'West'

print(p._name)