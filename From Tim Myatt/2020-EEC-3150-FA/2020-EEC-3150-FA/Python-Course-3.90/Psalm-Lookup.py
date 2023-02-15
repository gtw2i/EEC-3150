# Example line with the tab character between reference and verse
Chapter = input('Psalm chapter: ')
Verse = input('Psalm verse: ')

#Open the file bible-psalms.txt with file header fh
fh = open('bible-psalms.txt','r')

#For loop to iterate an implied fh.readline() to the eof
fh_eof = False
for pstring in fh:
    # Set boolean because we just read a new line
    fh_eof = True
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
    chapter = pstring[cindex:dindex]
    verse = pstring[dindex+1:tindex]
    text = pstring[tindex+1:len(pstring)]

    if Chapter == chapter and Verse == verse:
        print(text)
        break
    # Reset the boolean to see if we reach eof
    fh_eof = False

if not fh_eof:
    print('Chapter and/or verse do not exist.')

#Close the file and exit the program
fh.close()
exit()