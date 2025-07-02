""". Escreva um programa que leia do teclado dois números
inteiros nA e nB e leia também duas listas denominadas A e B com os tamanhos nA e nB,
respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam aceitos valores
repetidos. Em seguida, o programa deve juntar as duas em uma única lista R (resultante),
tomando o cuidado de que R não tenha valores duplicados. Veja o exemplo:
"""
nA = int(input("Entre com a quantidade de elementos na lista A: "))
nB = int(input("Entre com a quantidade de elementos na lista B: "))
a = []
b = []

while len(a) < nA:
    numA = int(input("Digite um número para a lista A: "))
    if numA not in a:
        a.append(numA)
    else:
        print("Esse número já existe na lista A!")

while len(b) < nB:
    numB = int(input("Digite um número para a lista B: "))
    if numB not in b:
        b.append(numB)
    else:
        print("Esse número já existe na lista B!")

c = list(set(a + b))
print("Lista resultante:", c)
