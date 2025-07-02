n = int(input("Entre com a quantidade de números: "))

for i in range(n):
    num = float(input(f"Digite o {i+1}º número real: "))
    
    if i == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

print(f"\nMenor número: {menor}")
print(f"Maior número: {maior}")
