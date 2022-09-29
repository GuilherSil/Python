def insereOrdenado(x, lista):
    for i in range(len(lista)):
        if x < lista[i]:
            lista.insert(i, x)
            return lista
    lista.append(x)
    return lista

vet = [1, 6, 10, 24, 25, 30, 45]
insereOrdenado(20, vet)
print(vet)
