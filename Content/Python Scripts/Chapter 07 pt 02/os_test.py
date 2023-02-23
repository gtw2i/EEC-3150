import os

# print the current working directory
cwd = os.getcwd()
print(cwd)

# print the contents of the cwd
contents1 = os.listdir()
print(contents1)

# let's read and print a file from contents1
# this might fail on your machine if contents1[0] is a folder, not a file
with open(contents1[0],'r') as f:
    for line in f.readlines():
        print(line.strip())

# print the contents of the parent directory
contents2 = os.listdir('..')
print(contents2)

"""
you can use os.mkdir('Test Folder') to create a directory called 
'Test Folder' in the current working directory. i'm writing it here
because I don't want y'all to accidentally create a directory
that you didn't intend. if you want to try it, copy it and paste
it outside this comment
"""