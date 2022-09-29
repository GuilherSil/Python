from contextlib import ContextDecorator


def maiorQueX(lista, x):
    contador = 0
    for i in lista:
        if i > x:
            contador += 1
    return contador

print(maiorQueX([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    
