n = 5

k = 0

x = []
for i in range(n):
    x.append([])
    for j in range(n):
        x[i].append(k)
        k += 1
    # end
# end

print(x)
print()

for i in range(n):
    print(x[i])