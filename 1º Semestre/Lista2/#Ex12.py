#Ex12
rm = int(input("Informe rm: "))
soma = 0

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

print("A soma dos números foi de: " , soma, ".")