def busca(vet, x):
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1

   

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


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(buscaBinaria(lista, 1)) 