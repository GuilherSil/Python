#Ex06

numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))

div = numA % numB

if div == 0:
    print (numA ," é divisível por ",numB)
else:
    print (numA, " não é divisível por ", numB)