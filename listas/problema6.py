n = int(input("Entre com um numero entre 0 e 50: "))
a = []
negativos =[]
positivos = []

if n <0 and n>50:
    print("O valor nao esta dentro do intervalo")
else:
    for i in range(n):
        num = int(input("Entre com um numero: "))
        a.append(num)
        if num < 0:
            negativos.append(num)
        else:
            positivos.append(num)
print("lista: ",a)
print("Positivos: ",positivos)
print("Negativos: ",negativos)