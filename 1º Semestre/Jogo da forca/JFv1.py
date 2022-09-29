def coloca_traco(word):
    aux = ""
    i = 0
    while i < len(word):
        if word[i] != " ":
            aux = aux + "_ "
        else:
            aux = aux + "  "
        i = i + 1    
    return aux 

def verifica_palavra(guess, word, secret):
    if guess == word:
        resp = ""
        for c in word:
            resp = resp + c + " "
        return resp    
    else:
        return secret    

def verifica_letra(guess, word, secret):
    resp = ""
    i = 0
    while i < len(word):
        if word[i] == guess:
            resp = resp + guess + " "
        else:
            resp = resp + secret[2 * i] + " "
        i = i + 1
    return resp            

palavra = "fruta do conde"
erros = 0

segredo = coloca_traco(palavra)

while erros < 6 and "_" in segredo:
    print(segredo)
    print("Erros: ", erros)
    chute = input("Letra: ")
    if len(chute) > 1:
        segredo = verifica_palavra(chute, palavra, segredo)    
    else:
        segredo = verifica_letra(chute, palavra, segredo)

    if not chute in palavra:
        erros = erros + 1

if erros >= 6:
    print("Você foi enforcado. A palavra era", palavra + ".")
else:
    print("Parabéns, você acertou! A palavra era", palavra + ".")            


    
