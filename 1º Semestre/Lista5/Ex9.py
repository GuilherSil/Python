#Ex14

#31 dias = 1 - 3 - 5 - 7 - 8 - 10 - 12
#30 dias = 4 - 6 - 9 - 11
#28/29 dias = 2

def verificadorData(dia,mes,ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        ano = "bissexto"
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia <= 31:
                return print("Data válida.")
            else:
                return print("Data inválida.")    
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia <= 30:
                return print("Data válida.")
            else:
                return print("Data inválida.")
        else:
            if dia <= 29:
                return print("Data válida.")
            else:
                return print("Data inválida.")
    elif ano != "bissexto":   
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia <= 31:
                return print("Data válida.")
            else:
                return print("Data inválida.")    
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia <= 30:
                return print("Data válida.")
            else:
                return print("Data inválida.")
        else:
            if dia <= 28:
                return print("Data válida.")
            else:
                return print("Data inválida.")


ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))
verificadorData(dia,mes,ano)

