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
    # Construct the reference string
    ref = 'Psalms ' + Chapter + ':' + Verse
    # Search for the line and extract the text
    if ref == pstring[0:len(ref)]:
        print(pstring[len(ref)+1:])
        break
    # Reset the boolean to see if we reach eof
    fh_eof = False

if not fh_eof:
    print('Chapter and/or verse do not exist.')

#Close the file and exit the program
fh.close()
exit()