def Soma2(lista, n):
    tupla = ()
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == n:
                if lista[i] and lista[j] in tupla:
                    continue
                else:
                    tupla += (lista[i], lista[j])
    return tupla            
                
    



lista = [2, 5, -7, 9, 3, 10, 15, 6]

print(Soma2(lista, 11))