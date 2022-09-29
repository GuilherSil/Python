def insere_branco(palavra):
    i = 0
    aux = ""
    while i < len(palavra):
        aux = aux + palavra[i] + " "
        i = i + 1
    return aux.strip()    

resp = insere_branco("Manga")  
resp = resp + "."
print(resp)      

s = resp.replace(" ", "")
print(s)