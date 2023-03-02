def get_ratios(x, y):
    
    ratios = []
    
    for i in range(len(x)): 
        try: 
            ratios.append(x[i]/y[i]) 
        except ZeroDivisionError: 
            ratios.append(float('nan'))
            print(f"Appending nan: y[{i}] = 0")
        except TypeError: 
            ratios.append(float('nan'))
            print(f"Appending nan: bad argument type")
        # end
    # end
            
    return ratios
# end

a = [1,2,3]
b = [1,0,'a']

c = get_ratios(a,b)
print(c)