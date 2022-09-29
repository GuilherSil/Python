mat = []
for i in range(0, 256):
    mat.append(i)
for i in range(len(mat)):
    if i <= 127:
        mat[i] = 0
    else:
        mat[i] = 255

print(mat)        