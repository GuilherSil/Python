#declarar variaveis
quantidadeAcumuladora = 0
agregadoAcumulador = 0
produtoItens = ""
precoQuantidade = ""
quantidade = 0


while quantidade >= 0:
    produto = str(input("Digite o nome do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço do produto: "))

    if quantidade > quantidadeAcumuladora:
        quantidadeAcumuladora = quantidade
        produtoItens = produto
    if quantidade * preco > agregadoAcumulador:
        agregadoAcumulador = quantidade * preco 
        precoQuantidade = produto


print("O produto {} teve o maior número de itens: {}".format(produtoItens, quantidadeAcumuladora))
print("O produto {} teve o maior valor agredado (preço * quantidade): R${}".format(precoQuantidade, agregadoAcumulador))            