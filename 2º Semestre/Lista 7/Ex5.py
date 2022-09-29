def maiorString(lista):
    maior = lista[0]
    for i in lista:
        if len(i) > len(maior):
            maior = i
    return maior

print(maiorString(("num","ta","legal","uuuh","ugaugauga")))   