n = int (input("Entre com um numero: "))
soma = 0

for num in range(n):
    y = int(input("Entre com um numero: "))
    impar = y%2
    if impar == 1:
        soma = soma + y
print(soma)