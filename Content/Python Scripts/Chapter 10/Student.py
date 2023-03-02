class Student:
    def __init__(self, name, univ, year, major):
        self._name = name
        self._univ = univ
        self._year = year
        self._major = major
    # end
# end

s = Student("John Smith", "TNU", "Freshman", "Physics")
            
print(vars(s))





