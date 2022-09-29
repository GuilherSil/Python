#Ex10


n = int(input("Digite o valor de n: "))
n1 = 1
acumulador = 1

# 1 2 3 4 5 6
while n >= 1:
    n1 = n1 * acumulador
    n = n - 1
    acumulador = acumulador + 1
    print(n1)

    
