fname = "YearTemp.txt"
with open(fname, 'r') as fhandle:
    lines = fhandle.readlines()
# end

years = []
temps = []


for i in range(4,len(lines)):
    line = lines[i].strip()
    x = line.split(',')
    years.append(int(x[0]))
    temps.append(float(x[1]))
# end

print(years)
print(temps)