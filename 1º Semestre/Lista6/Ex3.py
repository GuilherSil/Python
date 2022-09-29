def alterador(frase, letra):
    i = 0
    novaFrase = ""
    while i < len(frase):
        if letra.upper() in frase[i]:
            novaFrase = novaFrase + "*"
        elif letra.lower() in frase[i]:
            novaFrase = novaFrase + "*"
        else:
            novaFrase = novaFrase + frase[i]   
        i += 1               
    return novaFrase            


frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")
resp = alterador(frase, letra)
print(resp)       
    