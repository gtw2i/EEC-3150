import circle
import sphere

def area(side):
    return side**2

pi = 3 
print(pi, circle.pi, sphere.pi)
print(area(1), circle.area(1), sphere.area(1))