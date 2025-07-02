"""Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida, o programa deve juntar as duas listas em umaúnica com o tamanho 20.
"""
lis1=[]
lis2=[]
for i in range(10):
    lis1.append(input("Insira um valor: "))
for i in range(10):
    lis2.append(input("Insira um valor: "))
lis3 = lis1 + lis2
print(lis3)