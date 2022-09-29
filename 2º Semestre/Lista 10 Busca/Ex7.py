def busca(vet, x):
    lista = []
    for i in range(len(vet)):
        if vet[i] == x:
            lista.append(i)
    
    if lista != []:
        return lista
    else:
        return "Nenhum número encontrado"

print(busca([1, 2, 3, 4, 5, 1, 1, 8, 1, 10], 1))    