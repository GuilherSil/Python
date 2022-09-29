def intercalaOrdemCrescente(lista1, lista2):
    lista3 = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista3.append(lista1[i])
            i += 1
        else:
            lista3.append(lista2[j])
            j += 1
    while i < len(lista1):
        lista3.append(lista1[i])
        i += 1
    while j < len(lista2):
        lista3.append(lista2[j])
        j += 1
    return lista3
            
print(intercalaOrdemCrescente([1, 2, 3, 4, 5, 6, 7, 8, 19], [3, 5, 7, 9, 11, 13, 15, 17]))