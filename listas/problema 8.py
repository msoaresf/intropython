n = int(input("Ingresa un numero: "))
lista = []

for i in range(n):
    num = int(input("Ingresa un numero: "))
    if num not in lista:
        lista.append(num)
    else:
        listaremovidos.remove(num)