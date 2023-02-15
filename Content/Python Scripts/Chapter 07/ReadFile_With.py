fname = "FirstFile.txt"

with open(fname, 'r') as fhandle:
    string = fhandle.read()
    print(string)

with open(fname, 'r') as fhandle:
    lines = fhandle.readlines()
    print(lines)

with open(fname, 'r') as fhandle:
    for line in fhandle:
        print(line)

with open(fname, 'r') as fhandle:
    line = fhandle.readline()
    print(line)
    line = fhandle.readline()
    print(line)

with open(fname, 'r') as fhandle:
    line = fhandle.readline()
    while line:
        print(line)
        line = fhandle.readline()