class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def HaveBirthday(self):
        self._age += 1

p = Person("Bill", 50)

print(p._name, p._age)

p.HaveBirthday()

print(p._name, p._age)

print(vars(p))