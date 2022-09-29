#Ex13


import random

sorteado = random.randint(1,1000)

chute = int(input("Chute um número: "))
tentativas = 1

while chute != sorteado:
    if chute < sorteado:
        print("Tente um número maior.")
    elif chute > sorteado:
        print("Tente um número menor.")
    tentativas = tentativas + 1
    chute = int(input("Chute um número: "))    

print("Você acertou em", tentativas, "tentativas.")


