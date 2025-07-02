matriz = [] #defino matriz como uma lista
a = int(input("Entre com a qtt de linhas"))
b = int(input("Entre com a qtt de colunas"))

for i in range(a):
    linha = []
    for j in range(b):
        num = float(input("Entre com a nota do trabalho: "))
        linha.append(num)
    matriz.append(linha)
print(matriz)