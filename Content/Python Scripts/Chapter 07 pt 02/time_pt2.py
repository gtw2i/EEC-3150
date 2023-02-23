import time

# demo of sleep
print('sleeping 2 seconds...')
time.sleep(2)
print('done sleeping')

# demo of time
t1 = time.time()
print(f"time 1: {t1}")

# do something that takes a while
tot = 0
for i in range(10000000):
    tot += 1
# end

# get time again and measure the difference
t2 = time.time()
print(f"time 2: {t2}")
print(f"duration: {t2-t1} seconds")

# let's get the average time to do that sum
n = 10 # do the sum n times

# create a list of start, end, and duration times
starts = []
ends = []
durs = []
# do the sum n times
for j in range(n):
    # get starting times
    starts.append(time.time())
    # do the sum
    tot = 0
    for i in range(10000000):
        tot += 1
    # end
    # get ending times
    ends.append(time.time())
    # get durations as difference of start and end
    durs.append(ends[-1]-starts[-1])
# end

print(durs)

avg = sum(durs)/n
m1 = min(durs)
m2 = max(durs)

print(f"min duration: {m1} seconds")
print(f"avg duration: {avg} seconds")
print(f"max duration: {m2} seconds")

# if statements take a long time to run

# add only even numbers WITHOUT if statement
t1 = time.time()
tot = 0
for i in range(0,10000000,2):
    tot += 1
# end
t2 = time.time()
print(f"duration WITHOUT if: {t2-t1} seconds")

# add only even numbers WITH if statement
t1 = time.time()
tot = 0
for i in range(10000000):
#for i in range(0,10000000,2):
    if i%2 == 0:
        tot += 1
    # end
# end
t2 = time.time()
print(f"duration WITH if: {t2-t1} seconds")