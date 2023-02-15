n = 0xFFFFFF00
# Count all the zeros on the right, stop at 1
rightzeros = 0
for i in range (0,32):
    x = n & 0x00000001
    if x == 0:
        rightzeros += 1
        n = n >> 1
    else:
        break
# Count all the ones on the left, stop at 0
leftones = 0
for i in range (0, 32-rightzeros):
    x = n & 0x00000001
    if x == 1:
        leftones += 1
        n = n >> 1
    else:
        break
# The sum of left ones and right zeros must be 32
if (rightzeros + leftones != 32
        or rightzeros == 0
        or leftones == 0):
    print ('Invalid network mask')
else:
    print(leftones, rightzeros, 2**rightzeros)