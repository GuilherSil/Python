#Ex11


n = int(input("Digite n:"))

n1 = 1
n2 = 1
a = 3

print("\n1"+"\n1"+"\n2")

while a < n:
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    n3 = n2 + n1
    a = a + 1
    print (n3)

    


