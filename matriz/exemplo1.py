#como criar uma matriz onde cada [i][j] corresponde a i*j
l, c= 5, 5
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        linha.append(i*j)
    matriz.append(linha)
for i in range(l):
    print(matriz[i])