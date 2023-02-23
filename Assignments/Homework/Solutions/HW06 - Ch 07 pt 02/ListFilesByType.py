import os
import pickle as pk

contents = os.listdir()
print(contents)

files = {}
for f in contents:
    x = f.split('.')
    if x[1] in files.keys():
        files[x[1]].append(f)
    else:
        files[x[1]] = [f]
    # end
# end

print(files)

with open('FileTypes.pk', 'wb') as f:
    pk.dump(files, f)