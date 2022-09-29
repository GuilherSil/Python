n = int(input("Digite a quantidade n de produtos: "))

maiorPorcentual = 0
produtoPorcentual = 0
maiorAumento = 0
produtoAumento = 0
a = 1

while a <= n:
    precoAtual = float(input("Digite o preço ATUAL do produto: "))
    precoReajustado = float(input("Digite o preço REAJUSTADO do produto: "))
    if precoReajustado - precoAtual > maiorAumento:
        maiorAumento = precoReajustado - precoAtual
        produtoAumento = a


    porcentagem = ((precoReajustado - precoAtual) / precoAtual) * 100 
    if porcentagem > maiorPorcentual:
        maiorPorcentual = porcentagem
        produtoPorcentual = a 

    a = a + 1    



print("Seu {}º produto teve o maior aumento em reais (R${:.2f}).".format(produtoAumento, maiorAumento))
print("Seu {}º produto teve o maior aumento porcentual ({:.2f}%).".format(produtoPorcentual, maiorPorcentual)) 
    