#Name: Dr. Myatt
#Collaborators: None
#Date: 10/13/2020
#Description:  There are two inputs to this program: 1) a text file
#   called bible-psalms.txt that contains each verse of the book of
#   the Bible Psalms, one verse per line, and 2) a request of the user
#   for what verse number from Psalms (there are 2,461 total verses).
#   The output is the verse number specified by the user in the form:
#   Psalm c:v verse-text (where c is the chapter and v is the verse)
#
#Prompt the user for the verse number.
v = int(input('Verse # (1-2461): '))

#Open the file bible-psalms.txt with file header fh
fh = open('bible-psalms.txt','r')

#For loop to count from 0 through v-1, reading the next line of the file
for i in range(0,v):
    line = fh.readline()

#Print the result
print(line)

#Close the file and exit the program
fh.close()
exit()