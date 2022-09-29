with open("cacapalavra.txt", "r") as arquivo:
    xy = int(arquivo.readline())
    matriz = []
    for i in range(xy + 2):
        matriz.append(["@"] * (xy+2))
    
    
    for i in range(1,xy + 1):
        linha = arquivo.readline()
        auxlinha = 0
        for j in range(1,xy + 1):
            matriz[i][j] = linha[auxlinha]
            auxlinha += 1
        
    quantidadePalavras = arquivo.readline()
    listaPalavras = []
    for i in range(int(quantidadePalavras)):
       listaPalavras.append(arquivo.readline().strip())   

palavrasEncontradas = []
auxl = 0
auxc = 0

for palavra in listaPalavras:
    for l in range(xy + 2):
        for c in range(xy + 2):
            auxLetra = 0
            if palavra[auxLetra] == matriz[l][c]:
                auxl = l
                auxc = c
                posicaoL = l
                posicaoC = c
                try:
                    if palavra[auxLetra + 1] == matriz[auxl - 1][auxc - 1]:   
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Diagonal Superior Esquerda
                            auxLetra += 1
                            auxl -= 1
                            auxc -= 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Diagonal Superior Esquerda")
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl - 1][auxc]:  
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Cima
                            auxLetra += 1
                            auxl -= 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Cima")
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl - 1][auxc + 1]:  
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Diagonal Superior Direita
                            auxLetra += 1
                            auxl -= 1
                            auxc += 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Diagonal Superior Direita")
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl][auxc - 1]:  
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Esquerda
                            auxLetra += 1
                            auxc -= 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Esquerda")
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl][auxc + 1]:
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Direita
                            auxLetra += 1
                            auxc += 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Direita")       
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl + 1][auxc - 1]:    
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Diagonal Inferior Esquerda   
                            auxLetra += 1
                            auxl += 1
                            auxc -= 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Diagonal Inferior Esquerda")  
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl + 1][auxc]:    
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):  
                            #Baixo
                            auxLetra += 1
                            auxl += 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Baixo")   
                    auxl = l
                    auxc = c
                    auxLetra = 0
                    if palavra[auxLetra + 1] == matriz[auxl + 1][auxc + 1]:
                        while palavra[auxLetra] == matriz[auxl][auxc] and auxLetra < len(palavra):
                            #Diagonal Inferior Direita
                            auxLetra += 1
                            auxl += 1
                            auxc += 1
                            if auxLetra == len(palavra):
                                palavrasEncontradas.append(palavra)
                                print("Palavra: " + palavra + " - Linha: " + str(posicaoL) + " Coluna: " + str(posicaoC) + " - Direção: Diagonal Inferior Direita")
                except:
                    pass
                                        
print(palavrasEncontradas)
print(listaPalavras)
