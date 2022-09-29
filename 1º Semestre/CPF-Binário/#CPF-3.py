#CPF-3
#abc def ghi

cpf = int(input("Digite os 9 primeiros números do seu CPF: "))

i = cpf % 10
cpf = cpf // 10
h = cpf % 10
cpf = cpf // 10
g = cpf % 10
cpf = cpf // 10
f = cpf % 10
cpf = cpf // 10
e = cpf % 10
cpf = cpf // 10
d = cpf % 10
cpf = cpf // 10
c = cpf % 10
cpf = cpf // 10
b = cpf % 10
cpf = cpf // 10
a = cpf % 10
cpf = cpf // 10

v1 = 10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i
v1 = v1 % 11
if v1 < 2:
        v1 = 0
else:
    v1 = 11 - v1

v2 = 11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*v1 
v2 = v2 % 11   
if v2 < 2:
        v2 = 0
else:
    v2 = 11 - v2

print(v1, v2)   
print(a,b,c,d,e,f,g,h,i,v1,v2)         



