"""Escreva um programa que leia uma lista com N números inteiros, em que N é um número inteiro previamente digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que, quando essa situação
ocorrer, uma mensagem deve ser dada ao usuário. Por fim, exibir na tela a lista resultante."""
n = int(input("Entre com o valor de N:"))
lista = []
while len(lista) < n:
    num = int(input("Entre com um valor:"))
    if num in lista:
        print("Este numero ja existe na lista:")
    else:
        lista.append(num)
print(lista)