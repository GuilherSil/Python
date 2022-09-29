def mg(a, b):
    fatoracao = (a*b) ** (1/2)
    return fatoracao

valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))

resp = mg(valorA, valorB)
print ("A média geométrica de {} e {} é de: {}".format(valorA, valorB, resp))
    
    
                


