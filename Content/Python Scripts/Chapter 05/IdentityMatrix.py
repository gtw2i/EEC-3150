def identity(n):
    eye = []
    for i in range(n):
        eye.append([])
        for j in range(n):
            if i==j:
                eye[i].append(1)
            else:
                eye[i].append(0)
            # end
        # end
    # end
    
    return eye
# end

print(identity(3))