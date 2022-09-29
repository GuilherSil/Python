#Ex14

valorvista = float(input("Digite o valor a vista total: "))
valorparcela = float(input("Digite o valor da parcela: "))

valorparcelatotal = valorparcela * 10
desconto = valorparcelatotal - valorvista
porcentagem = desconto / 100 * (desconto - 1)

print("Com um desconto de ", porcentagem, "% por efetuar o pagamento a vista. Você recebeu um desconto de R$", desconto,)