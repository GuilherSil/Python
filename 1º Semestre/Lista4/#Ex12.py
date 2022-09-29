#Ex12


num = int(input("Informe num:"))
num_bkp = num
soma = 0

while num != 0:
    resto = num % 10
    num = num // 10
    soma = soma * 10 + resto

print(soma)
if soma == num_bkp:
    print("É palíndrome!")
else:
    print("Não é palíndrome.")        