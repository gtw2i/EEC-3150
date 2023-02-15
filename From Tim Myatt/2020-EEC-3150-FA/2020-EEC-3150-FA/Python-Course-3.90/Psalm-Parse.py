# Example line with the tab character between reference and verse
pstring = 'Psalms 92:11' + '\t' + 'Mine eyes also shall see...'
print('The string to parse is:', pstring)

# Find the position of the first space (e.g after the word Psalms)
cindex = 0
for c in pstring:
    cindex += 1
    if c == ' ': break
# Find the position of the colon separating the chapter & verse
dindex = 0
for c in pstring:
    if c == ':': break
    dindex += 1

# Find the position of the tab character after the reference
tindex = 0
for c in pstring:
    if c == '\t': break
    tindex += 1

#
print('cindex =', cindex, 'dindex =', dindex, 'tindex =', tindex)

chapter = pstring[cindex:dindex]
verse = pstring[dindex+1:tindex]
text = pstring[tindex+1:len(pstring)]

print('chapter =', chapter, 'verse =', verse)
print('text =', text)
