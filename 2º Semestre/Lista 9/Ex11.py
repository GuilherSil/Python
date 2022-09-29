import random
from socket import SOMAXCONN

matriz = []
i = 0
while i < 5:
    matriz.append([0] * 6)
    i += 1

for i in range(len(matriz) - 1):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(5, 10)

aux = 0
while aux <= len(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][aux]
    matriz[i][aux] = soma
    aux += 1
        

for i in matriz:
    print(i)        

maiorValor = 0
for i in range(len(matriz)):   
    for j in range(len(matriz[0])):
        if matriz[i][j] > maiorValor:
            maiorValor = matriz[i][j]

print(maiorValor)            