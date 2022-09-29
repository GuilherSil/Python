def verificaOrdem(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista3 = [3,6,1,2,8,4,1,2,7]

print(verificaOrdem(lista1))
print(verificaOrdem(lista2))
print(verificaOrdem(lista3))