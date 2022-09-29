import random

matriz = []
i = 0
while i < 5:
    matriz.append([0] * 6)
    i += 1

for i in range(len(matriz)):
    for j in range(len(matriz[0]) - 1):
        matriz[i][j] = random.randint(5, 10)


for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[0])):
        soma += matriz[i][j]
    matriz[i][j]= soma

for i in matriz:
    print(i)