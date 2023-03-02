def divide(x, y):
    
    try:
        print("try")
        result = x/y
    except ZeroDivisionError:
        print("except")
    else:
        print("else")
    finally: 
        print('finally')  
 
divide(3, 2)
print()
divide(3, 0)