def inverteString(palavra):
    acumulador = len(palavra)
    acumuladorInversa = ""
    while acumulador > 0:
        acumuladorInversa = acumuladorInversa + palavra[acumulador-1]
        acumulador = acumulador - 1
    return acumuladorInversa 


palavra = str(input("Digite alguma coisa: "))     
resp = inverteString(palavra)      
print(resp)