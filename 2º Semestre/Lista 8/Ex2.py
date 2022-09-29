import random

aux = int(input("Digite a quantidade de números "))
lista = [0] * aux
for i in range(aux):
    lista[i] = random.randint(1, 1001)

print(lista)    