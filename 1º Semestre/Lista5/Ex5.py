def verificarNumPerfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma == num:
        return True
    else:
        return False

aux = 1
while aux <= 50000:
    if verificarNumPerfeito(aux):
        print(aux)
    aux += 1
          