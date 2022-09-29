def encaixaNum(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    auxNum1 = len(num1)
    auxNum2 = len(num2)
    acumulador = ""
    for aux in range(auxNum1 - auxNum2, auxNum1):
        acumulador += num1[aux]
    if num2 in acumulador:
        return True
    else:
        return False

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if encaixaNum(num1, num2) == True:
    print("Encaixa.")
else:
    print("Não encaixa.")   