lista = [""] * 10
for i in range(10):
    lista[i] = input("Digite uma string: ")

novaLista = []
aux = 9
while aux >= 0:
    novaLista.append(lista[aux])
    aux -= 1

print(novaLista)
