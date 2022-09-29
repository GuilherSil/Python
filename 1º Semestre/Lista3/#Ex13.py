#Ex13

#31 dias = 1 - 3 - 5 - 7 - 8 - 10 - 12
#30 dias = 4 - 6 - 9 - 11
#28 dias = 2

mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        print("Data válida.")
    else:
        print("Data inválida.")    
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        print("Data válida.")
    else:
        print("Data inválida.")
else:
    if dia <= 28:
        print("Data válida.")
    else:
        print("Data inválida.")