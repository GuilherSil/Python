def mediaFaturamento():
    print("---! Média de faturamento mensal da Empresa Melhoras Compras Varejo !---\n")
    meses = int(input("Digite o número de meses: "))
    soma = 0
    contadorMeses = 1
    for aux in range(meses):
        valores = float(input("Digite o valor do faturamento do {}º mês: ".format(contadorMeses)))
        soma += valores
        contadorMeses += 1
    media = soma / meses
    return media
    
resp = mediaFaturamento()
print("A média de faturamento mensal é de: R${:.2f}".format(resp))