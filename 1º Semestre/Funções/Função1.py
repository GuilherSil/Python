def mmc(a, b):
    aux_mmc = a
    while a % aux_mmc != 0 or b % aux_mmc != 0:
        aux_mmc = aux_mmc - 1
    return aux_mmc

res = mmc(302,466)
print("MMC {}".format(res))    
        