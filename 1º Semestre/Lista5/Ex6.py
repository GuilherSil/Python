def contaDigitosDiferentes(num):
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    contador7 = 0
    contador8 = 0
    contador9 = 0

    IntToStr = str(num)
    rangeNum = len(IntToStr)
    for aux in range(0, rangeNum):
            if IntToStr[aux] == "1":
                contador1 += 1
            elif IntToStr[aux] == "2":
                contador2 += 1
            elif IntToStr[aux] == "3":
                contador3 += 1
            elif IntToStr[aux] == "4":
                contador4 += 1
            elif IntToStr[aux] == "5":
                contador5 += 1 
            elif IntToStr[aux] == "6":
                contador6 += 1
            elif IntToStr[aux] == "7":
                contador7 += 1
            elif IntToStr[aux] == "8":
                contador8 += 1
            elif IntToStr[aux] == "9":
                contador9 += 1
    return [contador1, contador2, contador3, contador4, contador5, contador6, contador7, contador8, contador9] 

num1 = int(input("Digite uma sequencia 'A' numérica: "))
num2 = int(input("Digite outra sequencia 'B' numérica: "))
if contaDigitosDiferentes(num1) == contaDigitosDiferentes(num2):
    print("A sequencia 'A' e 'B' é uma permutação")
else:
    print("Não é uma permutação") 

resp = contaDigitosDiferentes(num1)
print(resp) 
resp2 = contaDigitosDiferentes(num2)
print(resp2)          