""" Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-a na tela na ordem inversa à ordem de leitura."""
lista = []
for i in range(10):
    lista.append(i)
print(lista)
print(lista[::-1])