def melhoresAvaliacoes():
    print("---! Produtos mais bem avaliados da Empresa Melhoras Compras Varejo !---\n")
    acumuladorProdutos = ""
    produto = ""
    avaliacao = 0.01
    maiorAvaliacao = 0
    while avaliacao != 0 and produto != "Final":
        produto = input("Digite o nome do produto: ")
        avaliacao = float(input("Digite a avaliação do produto: ")) 
        if maiorAvaliacao == avaliacao:
            acumuladorProdutos += produto + "\n"
        if maiorAvaliacao < avaliacao:
            maiorAvaliacao = avaliacao
            acumuladorProdutos = produto + "\n"             
    return acumuladorProdutos        

resp = melhoresAvaliacoes()
print("Os produtos mais bem avaliados são:\n{}".format(resp))
    
