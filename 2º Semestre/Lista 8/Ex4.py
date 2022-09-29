n = int(input("Digite a quantidade de números: "))
lista = [0] * n
for i in range(n):
    lista[i] = int(input("Digite um número: "))

for i in range(n):
    print(lista[i] + lista[i-1])
    