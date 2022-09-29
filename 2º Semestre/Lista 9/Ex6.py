def busca(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                return [i, j]
    return [-1, -1]    

matriz = [
    [5, 6, 8, 12, 19, 20, 56],
    [4, -3, 16, 19, 17, 15, 1],
    [0, 8, 12, 15, -5, -4, 2]
]

print(busca(matriz, 56))
print(busca(matriz, -4))
print(busca(matriz, -10))