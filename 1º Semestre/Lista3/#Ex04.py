#Ex04

time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
time1gols = int(input("Quantos gols fez o primeiro time: "))
time2gols = int(input("Quantos gols fez o segundo time: "))

if (time1gols > time2gols):
    print (time1, "foi o vencedor com ", time1gols, " gols.")
elif (time2gols > time1gols):
    print (time2, "foi o vencedor com ", time2gols, " gols.")
else:
    print("Empate.")