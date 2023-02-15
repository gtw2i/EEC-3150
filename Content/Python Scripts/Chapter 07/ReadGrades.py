fname = "Grades.txt"
with open(fname, 'r') as fhandle:
    grades = []
    for line in fhandle:
        grades.append(int(line))
    # end
# end

print(grades)