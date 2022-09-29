#Ex05


divisor = 1

n = int(input("Digite um valor positivo inteiro: "))

while (divisor != n):
    div = n % divisor

    if(div == 0):
        print(divisor)

    divisor = divisor + 1    


