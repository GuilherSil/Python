#Ex09  


from cmath import pi


d = int(input("Digite o montante em dinheiro inicial: "))
j = int(input("Digite o juros mensal: "))
t = int(input("Digite o período passado em meses: "))

while(t > 0):
    d = d + (d * (j / 100))
    t = t - 1

print("O valor final é {:.2f}".format(d))    
