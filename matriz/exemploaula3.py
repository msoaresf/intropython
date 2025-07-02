#media de cada linha da coluna

matriz = [[1,2,3],[2,4,8],[3,6,9]]
tamMatriz = len(matriz)

for i in range (tamMatriz):
    soma = matriz[i][0]
    for j in range (1,len(matriz[0])):
         soma = soma + matriz[i][j]
    media = soma / tamMatriz
    print("Media da linha {}: {}".format(i,media))
