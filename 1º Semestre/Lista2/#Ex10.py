#Ex10

distancia = float(input("Digite a distância em metros: "))
tempo = float(input("Digite o tempo em segundos: "))

#vm = vdist/vtemp

vm = distancia / tempo
vmkm = vm * 3.6

print("A velocidade média em m/s foi de:", vm, "m/s. E em km/h de:", vmkm, "km/h.")