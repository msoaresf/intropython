matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        num = int(input("Entre com o [{}][{}]: ".format(i+1,j+1)))
        linha.append(num)
    matriz.append(linha)
    print(linha)
print(matriz)

for i in range(2):
    for j in range(3):
        maior = matriz[i][j]
