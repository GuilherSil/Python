cedula = int(input("Digite o valor da cédula: "))
moeda1 = int(input("Digite o valor da 1ª moeda: "))
moeda2 = int(input("Digite o valor da 2ª moeda: "))

conf = 0
acumulador = 0
multiplicador = 1

while conf != cedula:
    while acumulador <= cedula:
        acumulador2 = 1
        if (moeda1 * acumulador) / cedula == 1:
            quantidadeMoeda1 = acumulador
            acumulador = cedula + 2
            conf = cedula
            print("Troca possível: {} moeda(s) de {} e {} moeda(s) de {}".format(quantidadeMoeda1, moeda1, quantidadeMoeda2, moeda2)) 


        while acumulador2 <= cedula:
            if ((moeda1 * acumulador) + moeda2 * acumulador2) / cedula == 1:
                quantidadeMoeda1 = acumulador
                quantidadeMoeda2 = acumulador2 
                acumulador = cedula + 2
                acumulador2 = cedula + 2
                conf = cedula
                print("Troca possível: {} moeda(s) de {} e {} moeda(s) de {}".format(quantidadeMoeda1, moeda1, quantidadeMoeda2, moeda2)) 


            acumulador2 = acumulador2 + 1

       
        acumulador = acumulador + 1
        if acumulador == cedula + 1:
            conf = cedula
            print("Não é possível fazer a troca")