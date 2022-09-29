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

n = 2
primos = 1
while primos <= 100:
    resp = confPrimo(n)
    if resp == True:
        print("O número {} é primo. ({})".format(n, primos))
        primos = primos + 1
    n += 1    



