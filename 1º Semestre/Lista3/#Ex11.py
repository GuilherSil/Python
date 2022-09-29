#Ex11

preco = float(input("Digite o preço do produto: "))
print ("Para pagamentos a vista em dinheiro ou cheque, recebe 10% de desconto. (1)")
print ("Para pagamentos a vista no cartão de crédito, recebe 5% de desconto. (2)")
print ("Para pagamentos em duas vezes, não recebe desconto. (3)")
print ("Para pagamentos em quatro vezes, juros de 7%. (4)")
formapagamento = int(input("Digite o código da forma de pagamento: "))

if formapagamento == 1:
    print ("Quantidade a ser paga: R$", preco * 0.90)
elif formapagamento == 2:
    print ("Quantidade a ser paga: R$", preco * 0.95)
elif formapagamento == 3:
    print ("Quantidade a ser paga: 2x R$", preco * 0.50) 
elif formapagamento == 4:
    print ("Quantidade a ser paga: 4x R$", (preco * 1.07) / 4)       
else:
    print ("Código de pagamento não registrado.")
