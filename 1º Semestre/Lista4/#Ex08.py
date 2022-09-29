#Ex08


from re import A


n = int(input("Digite um número para descobrir se ele é primo: "))
a = 1
primo = 0

while (a <= n):
    if(n % a == 0):
        primo = primo + 1
    a = a + 1    


if(n == 1):
    print("É número primo!")
elif(primo == 2):
    print("É número primo!")
else:
    print("Não é número primo.")