import re
import time

def WithRegex():
    with open('Birthdays.txt','r') as f:
        text = f.read()
    # end
    
    pattern = r"\d{2}/\d{2}/\d{4}"
    bdays = re.findall(pattern, text)
    
    pattern = r"[A-Z][a-z]+ [A-Z][a-z]+"
    names = re.findall(pattern, text)
    
    d = {}
    for i,j in zip(names,bdays):
        d[i] = j
    # end
    
    return d
# end

def WithoutRegex():
    with open('Birthdays.txt','r') as f:
        lines = f.readlines()
    # end
    
    d = {}
    for line in lines:
        x = line.split(':')
        d[x[0].strip()] = x[1].strip()
    # end
    
    return d
        
# end

def GetAge(date, bday):
    date2 = date.split('/')
    date2 = list(map(int,date2))
    #print(date2)
    
    bday2 = bday.split('/')
    bday2 = list(map(int,bday2))
    #print(bday2)
    
    mdiff = date2[0] - bday2[0]
    ddiff = date2[1] - bday2[1]
    ydiff = date2[2] - bday2[2]
    
    if mdiff > 0 and mdiff > 0:
        return ydiff
    else:
        return ydiff-1
    # end
    
# end

celebs1 = WithRegex()
celebs2 = WithoutRegex()

today = time.localtime()
y = today[0]
m = today[1]
d = today[2]

today = f"{m:02d}/{d:02d}/{y}"

ks = celebs1.keys()
for k in ks:
    age = GetAge(today, celebs1[k])
    print(f"{k} is {age} years old")
# end