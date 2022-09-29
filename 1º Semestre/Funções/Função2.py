def mdc(a, b):
    div = a
    while a % div != 0 or b % div != 0:
        div = div - 1
    return div

r = mdc(18, 46)
print(r)