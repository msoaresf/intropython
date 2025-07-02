#como identificar e imprimir o maior valor de uma linha da matriz
matriz = [[2,5,6],[9,8,2],[3,4,5]]

for i in range (len(matriz)):
    maior = matriz[i][0]
    for j in range (1,len(matriz[0])):
     if maior < matriz[i][j]:
         maior = matriz[i][j]
    print("O maior numero da matriz {}:".format(i+1),maior)
