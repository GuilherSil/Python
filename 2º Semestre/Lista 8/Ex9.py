def numerosRepetidos(listaA, listaB):
    listaC = []
    for i in listaA:
        if i in listaB:
            listaC += [i]
    return listaC

print(numerosRepetidos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3,5,7,9,51,23,11,13]))


