def confPrimo(n):
    acumulador = n
    primo = 0
    while acumulador >= 1:
        if n % acumulador == 0:
            primo = primo + 1
        acumulador = acumulador - 1
    if n == 1:
        return True
    elif primo == 2:
        return True
    else:    
        return False

n = int(input("Digite o valor de N: "))
resp = confPrimo(n)
if resp == True:
    print("O número é primo.")
else:
    print("O número não é primo.")

