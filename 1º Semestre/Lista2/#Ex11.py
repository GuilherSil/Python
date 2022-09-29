#Ex11

salarioanterior = float(input("Digite o valor do salário anterior: "))
salarionovo = float(input("Digite o valor do salário agora: "))

dif = salarionovo - salarioanterior
porcentagem = salarioanterior * (dif / 100)

print("Salário antes do aumento:R$", salarioanterior, ". Salário depois do aumento:R$", salarionovo, ". Houve um aumento de R$", dif, ", que refere a um aumento de ", porcentagem, "%.")