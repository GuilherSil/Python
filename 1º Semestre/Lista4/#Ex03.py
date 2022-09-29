#Ex03


ac = 0
medianota = 0
mais5 = 0
menos5 = 0

alunos = int(input("Digite o número de alunos: "))

while ac != alunos:
    ac = ac + 1

    nota = float(input("Digite a nota do aluno: "))
    medianota = nota + medianota

    if (0 <= nota < 5):
        menos5 = menos5 + 1
    else:
        mais5 = mais5 + 1    


media = medianota / alunos

print("A média das notas da turma foi de ", media)
print(menos5,"Alunos tiraram nota menor que 5.\n ", mais5, "Alunos tiraram nota maior que 5.")   