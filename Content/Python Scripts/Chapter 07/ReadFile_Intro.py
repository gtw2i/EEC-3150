fname = "FirstFile.txt"

fhandle = open(fname, 'r') 

string = fhandle.read()
print(string)

fhandle.close() 