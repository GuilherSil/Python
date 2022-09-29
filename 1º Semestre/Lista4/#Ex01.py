#Ex01

ac = 0

num = int(input("Digite nº: "))      
while num != 0:
    resto = num % 2
    if resto == 0:
        ac = ac + num
    num = int(input("Digite nº: "))

print("A soma dos pares vale: ", ac)

 