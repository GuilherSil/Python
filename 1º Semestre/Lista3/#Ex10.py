#Ex10

import math

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

delta = B ** 2 - 4*A*C

if delta >= 0:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    print ("x1:",x1 ," x2:",x2)
else:
    print ("Sem raízes reais. Delta < 0.")    