a = []
b = []
c = []
for i in range (3):
    x = int(input("Entre com os valores {} da lista: "))
    z = int(input("Entre com os valores da lista: "))
    a.append(x)
    b.append(z)
    c.append(a[i]**2)
print(a)
print(b)
print(c)