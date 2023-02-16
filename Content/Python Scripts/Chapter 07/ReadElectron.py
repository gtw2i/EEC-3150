with open('h2o.txt','r') as f:
    lines = f.readlines()
# end

length = len(lines)

ind = 0
while lines[ind].split(' ')[0] != 'CENTRE' and ind < length-1:
    ind += 1
# end

centerLines = []
while lines[ind].split(' ')[0] == 'CENTRE' and ind < length-1:
    centerLines.append(lines[ind])
    ind += 1
# end

print(centerLines)

centers = []
for line in centerLines:
    x = line.split('ASSIGNMENTS')[1].strip()
    print(x)
    









