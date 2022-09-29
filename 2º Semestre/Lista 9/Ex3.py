import random


matriz = []
i = 0
while i < 5:
    matriz.append([0] * 7)
    i += 1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(0, 1000)    

for i in range(len(matriz)):
    print(matriz[i])