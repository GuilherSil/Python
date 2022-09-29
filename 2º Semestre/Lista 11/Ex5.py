def bubbleSort(lista, i):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                print(lista[i])
                print(lista[j])
                lista[i], lista[j] = lista[j], lista[i]
    return lista        
            

lista = [10, 15, 8, 19 ,30 ,12 ,84, 5, 10, 17]
print(bubbleSort(lista, 0))