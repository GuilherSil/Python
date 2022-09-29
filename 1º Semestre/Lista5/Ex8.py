def encaixaNum(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    auxNum1 = len(num1)
    auxNum2 = len(num2)
    if num1 in num2:
        return print("A é segmento de B")
    elif num2 in num1:
        return print("B é segmento de A")
    else:
        return print("Um não é segmento do outro")    


num1 = int(input("Digite um número (A): "))
num2 = int(input("Digite outro número (B): "))

resp = encaixaNum(num1, num2)
  