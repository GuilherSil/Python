def mediaAritmetica(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma/len(lista)

print(mediaAritmetica((5,5,5,5,5)))