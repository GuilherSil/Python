#Ex05

diastrabalhados = int(input("Digite a quantidade de dias úteis no mês: "))
horastrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorhora = float(input("Digite o valor da hora (formato xx.xx): "))

diastrabalhados = diastrabalhados * 8
horaextra = horastrabalhadas - diastrabalhados
devereceber = horaextra * valorhora

if (diastrabalhados == horastrabalhadas):
    print("Sem horas extras.")
    print("Receberá R${:2f}" .format(diastrabalhados * valorhora))
elif (diastrabalhados < horastrabalhadas):
    print("Tendo feito ", horaextra, " horas além da jornada mensal, você receberá R${:2f}".format(devereceber))
    print("Recebendo um total de R${:2f}" .format((horastrabalhadas * valorhora) ))    