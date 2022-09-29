def confPrimo(n):
    acumulador = n
    primo = 0
    while acumulador >= 1:
        if n % acumulador == 0:
            primo = primo + 1
        acumulador = acumulador - 1
    if n == 1:
        return print("O número é primo!")
    elif primo == 2:
        return print("O número é primo!")
    else:    
        return print("O número não é primo.")

n = int(input("Digite o valor de N: "))
resp = confPrimo(n)                   
