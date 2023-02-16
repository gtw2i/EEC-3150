with open('587722984435351614_combined.txt','r') as f:
    lines = f.readlines()
# end

lines = lines[:1294]

params = []
fits   = []
for line in lines:
    x = line.split('\t')
    fits.append( float(x[0].split(',')[1]) )
    params.append(list(map(float,x[1].split(','))))
# end