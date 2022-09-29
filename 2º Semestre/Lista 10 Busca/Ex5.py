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

def Soma2(lista, n):
    listaResp = []
    tupla = ()
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == n:
                if lista[i] and lista[j] in tupla:
                    continue
                else:
                    tupla += (lista[i], lista[j])
                    listaResp.append("("+str(lista[i])+" e "+str(lista[j])+")")
    return listaResp 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Soma2(lista, 11))