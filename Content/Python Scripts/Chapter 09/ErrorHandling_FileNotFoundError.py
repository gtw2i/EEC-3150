contents = []

for i in range(4):
    fname = "file_" + str(i+1) + ".txt"
    try:
        with open(fname,'r') as f:
            contents.append( f.read() )
        # end
        print(f"{fname} was read successfully")
    except FileNotFoundError:
        print(f"{fname} doesn't exist")
        contents.append( '' )
    # end
# end
print()

for c in contents:
    print(c)