def buscaBinaria(vet,x):
    inicio = 0
    fim = len(vet) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vet[meio] > x:
            fim = meio - 1
        elif vet[meio] < x:
            inicio = meio + 1
        else:
            return meio
    return -1  

def eliminaRepetidos(lista):
    lista2 = []
    for i in range(len(lista)):
        if buscaBinaria(lista2, lista[i]) == -1:
            lista2.append(lista[i])
    return lista2


lista = [1, 2, 2, 3, 5, 5, 6, 8, 8, 9, 10]    
print(eliminaRepetidos(lista))