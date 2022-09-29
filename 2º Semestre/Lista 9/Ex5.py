def soma(matriz):
    somaPos = 0
    somaNeg = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                somaPos += matriz[i][j]
            else:
                somaNeg += matriz[i][j]
    tuplaPosNeg = (somaPos, somaNeg)            
    return tuplaPosNeg

matriz = [
    [5, 6, 8, 12, 19, 20, 56],
    [4, -3, 16, 19, 17, 15, 1],
    [0, 8, 12, 15, -5, -4, 2]
]   

print(soma(matriz))