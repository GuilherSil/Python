def verificaCodigoBarras():
    print("---! Verificador de Código de Barras da Empresa Melhoras Compras Varejo !---\n")
    codigo = input("Digite o código de barras do produto: ")
    aux = 0
    contadorDigitos = 0
    while aux < len(codigo):
        if codigo[aux].isdigit():
            contadorDigitos += 1   
        aux += 1
    return contadorDigitos


resp = verificaCodigoBarras()
print("A quantidade de digitos no código de barras é: {}".format(resp))    