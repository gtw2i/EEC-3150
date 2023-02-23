import time

# get local or GM time as a struct_time
now = time.localtime()
#now = time.gmtime()
print(now)
print()

year  = now[0]
month = now[1]
day   = now[2]
# there's more elements than just these three

# print elements of a struct_time object using string formatting
print(f"year: {year}")
print(f"month: {month}")
print(f"day: {day}")
print(f"date: {month}/{day}/{year}")

