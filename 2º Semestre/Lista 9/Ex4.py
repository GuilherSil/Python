def somaPos(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                soma += matriz[i][j]
    return soma


matriz = [
    [5, 6, 8, 12, 19, 20, 56],
    [4, -3, 16, 19, 17, 15, 1],
    [0, 8, 12, 15, -5, -4, 2]
]    

print(somaPos(matriz))