#Ex04


positivos = 0
negativos = 0

n = int(input("Digite a quantidade de números: "))

while (n != 0):
    numero = float(input("Digite o valor do número: "))

    if (numero < 0):
        negativos = negativos + 1
    elif (numero > 0):
        positivos = positivos + 1

    n = n - 1    

print(negativos, "números negativos - ", positivos, "números positivos.")            