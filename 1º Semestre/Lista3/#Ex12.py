#Ex12

media1 = float(input("Digite a média do primeiro semestre: "))
media2 = float(input("Digite a média do segundo semestre: "))
aulas = int(input("Insira a quantidade de aulas do ano: "))
presenca = int(input("Insira quantas aulas o aluno teve presença: "))

presencaminima = aulas * 0.7
mediaano = (media1 * 0.4) + (media2 * 0.6)

if presenca < presencaminima:
    print ("Reprovado por faltas.")
elif presenca > presencaminima:
    if mediaano < 5:
        print ("Reprovado. Média de ", mediaano)
    elif mediaano >= 5 and mediaano < 7:
        print ("Aluno de exame. Média de ", mediaano)
    else:
        print("Aluno aprovado. Média de ", mediaano)
