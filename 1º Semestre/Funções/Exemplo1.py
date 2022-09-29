#Exemplo01
num1 = int(input("Digite o valor de a: "))
num2 = int(input("Digite o valor de b: "))

n = 1
mmc = 0

while n != 0:
    if num1 * n == num2 * n:
        mmc = n
        n = 0
n = n + 1

print(mmc)        