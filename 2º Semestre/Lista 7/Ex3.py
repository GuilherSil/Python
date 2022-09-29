def maiorValor(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

intPosit = (135,6486,5156,26648,169213,89798,1321,4894,999999999,131465,1000000000)    
print(maiorValor(intPosit))