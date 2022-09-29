n = int(input("Digite o valor de n: "))

contador = 0
num0 = -40028942297

while n >= 1:
    contador = contador + 1
    num1 = int(input("Digite um valor inteiro: "))
    if num1 == num0:
        contador = contador - 1
        
    num0 = num1
    n = n - 1
    

print("Segmentos de números iguais consecutivos: ", contador)             