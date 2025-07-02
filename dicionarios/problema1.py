"""Escreva um programa que permaneça em laço lendo números
inteiros do teclado. Esse laço termina quando for digitado zero ou qualquer valor negativo. O
programa deve contar quantas vezes cada valor positivo foi digitado. Ao término do laço de
leitura o programa deve mostrar quais valores foram digitados e quantas vezes cada um. Use
um dicionário para resolver esse problema."""
d = {}
while True:
    num = int(input("Entre com o numero: "))
    if num <= 0:
        break
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
print(d)

