min = int(input("Ingresa un numero: "))
max = int(input("Ingresa un numero: "))
lista = []

if min > max:
    print("El numero es mayor a el menor")
else:
    for i in range(min,max):
        res = i%7
        if res == 0:
            lista.append(i)
        else:
            print("Numero nao é divisivel")
print(lista)
