def verificaCodigoBarras():
    print("---! Verificador de Código de Barras da Empresa Melhoras Compras Varejo !---\n")
    codigo = input("Digite o código de barras do produto: ")
    aux = 0
    contadorDigitos = 0
    while aux < len(codigo):
        if codigo[aux] == "1":
            contadorDigitos += 1
        elif codigo[aux] == "2":
            contadorDigitos += 1
        elif codigo[aux] == "3":
            contadorDigitos += 1
        elif codigo[aux] == "4":
            contadorDigitos += 1
        elif codigo[aux] == "5":
            contadorDigitos += 1 
        elif codigo[aux] == "6":
            contadorDigitos += 1
        elif codigo[aux] == "7":
            contadorDigitos += 1
        elif codigo[aux] == "8":
            contadorDigitos += 1
        elif codigo[aux] == "9":
            contadorDigitos += 1
        elif codigo[aux] == "0":
            contadorDigitos += 1    
        aux += 1
    return contadorDigitos


resp = verificaCodigoBarras()
print("A quantidade de digitos no código de barras é: {}".format(resp))    