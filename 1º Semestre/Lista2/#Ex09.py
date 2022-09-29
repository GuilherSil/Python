#Ex09

nvpreco = 0

preco = float(input("Informe o preço do produto: "))
desconto = float(input("Informe a % do desconto: "))

desconto = desconto / 100


print("Desconto dado: ", preco * desconto  )
print("O valor com o desconto ficou de: ", preco *(1-desconto))

#Se fosse um aumento no preço no lugar do desconto ^^^^ somente o sinal "-" mudaria para "+".