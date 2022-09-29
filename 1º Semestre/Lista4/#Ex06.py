#Ex06


nAluno = 0
m20 = 0
m50 = 0
m70 = 0
menor = 70
maior = 0


while (nAluno < 20):
    
    nota = float(input("Digite a nota do aluno:" ))
    if(nota < menor):
        menor = nota

    if(nota > maior):
        maior = nota

    if(nota < 21):
        m20 = m20 + 1
    elif(nota < 51):
        m50 = m50 + 1
    else:
        m70 = m70 + 1            
    

    nAluno = nAluno + 1


print(m20, "alunos tiraram nota menor que 20.({})".format(m20 * 100 / 20))  
print(m50, "alunos tiraram nota entre 21 e 50.({})".format(m50 * 100 / 20))  
print(m70, "alunos tiraram nota maior que 50.({})".format(m70 * 100 / 20))   
print("A maior nota foi ", maior)
print("A menor nota foi ", menor)    

