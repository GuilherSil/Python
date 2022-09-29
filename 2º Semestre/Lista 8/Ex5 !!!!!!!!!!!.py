def confOrdem(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

if confOrdem([1,2,3]) == True:
    print("Ordem crescente")
else:
    print("Ordem não crescente")                                    