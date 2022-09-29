#Escreva uma função em Pytho nque recebe como parâmetros uma String e retorna a quantidade de vogais existentes nessa String.
def retornaVogais(string):
    stringNova = string.upper()
    acumulador = 0
    quantidadeVogais = 0
    while acumulador < len(string):
        if stringNova[acumulador] == "A" or stringNova[acumulador] == "E" or stringNova[acumulador] == "I" or stringNova[acumulador] == "O" or stringNova[acumulador] == "U":
            quantidadeVogais += 1   
        acumulador += 1       
    return quantidadeVogais    
    

palavra = str(input("Digite alguma coisa: "))
retorno = retornaVogais(palavra)
print(retorno)