import random


matriz = []
i = 0
while i < 30:
    matriz.append([0] * 50)
    i += 1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(0, 200)  

conta = [0] * 201
   
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        conta[matriz[i][j]] += 1

print(conta)            
