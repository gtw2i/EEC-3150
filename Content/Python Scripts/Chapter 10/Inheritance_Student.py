class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def HaveBirthday(self):
        self._age += 1

class Student(Person):
    
    def __init__(self, name, age, univ, year, major):
        super().__init__(name,age)
        self._univ = univ
        self._year = year
        self._major = major

p = Person("bill", 20)
s = Student("bill", 20, "TNU", "Fr", "Math")
print(p._age,s._age)
p.HaveBirthday()
s.HaveBirthday()
print(p._age,s._age)


