#Ex02


ac = 0
medianota = 0

alunos = int(input("Digite o número de alunos: "))

while ac != alunos:
    ac = ac + 1

    nota = float(input("Digite a nota do aluno: "))
    medianota = nota + medianota

media = medianota / alunos

print("A média das notas da turma foi de ", media)    