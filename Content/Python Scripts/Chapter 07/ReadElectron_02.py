f = open('nh3.txt','r')

centerLines = []
typeLines = []
expLines = []

line = f.readline()
while line:
    if line.split(' ')[0] == 'CENTRE':
        centerLines.append(line)
    if line.split(' ')[0] == 'TYPE':
        typeLines.append(line)
    if line.split(' ')[0] == 'EXPONENTS':
        expLines.append(line)
    
    line = f.readline()
# end

f.close()

centers = []
for line in centerLines:
    x = line.split('ASSIGNMENTS')[1].strip().replace('  ',' ').split(' ')
    centers.extend(x)
# end
centers = list(map(int,centers))
print(centers)

types = []
for line in typeLines:
    x = line.split('ASSIGNMENTS')[1].strip().replace('  ',' ').split(' ')
    types.extend(x)
# end
types = list(map(int,types))
print(types)

exps = []
for line in expLines:
    x = line.replace('D','e').split('EXPONENTS')[1].strip().replace('  ',' ').split(' ')
    exps.extend(x)
# end
exps = list(map(float,exps))
print(exps)




