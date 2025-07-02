n =int(input("Entre com um numero: "))
total = 0
media = 0
maior = 0
menor = 0
n= 0
i = 0
while n <= 999:
    temp = float(input("Entre com um numero: "))
    total= total + temp
    n = n + 1
    media = total/n
    x = temp
    if temp > maior:
        maior = temp
    elif temp < menor:
        menor= temp
    else:
        menor = temp
        maior = temp
print(maior)
print(menor)
print(media)