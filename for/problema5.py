mini = int(input("Entre com o valor minimo"))
maxi = int(input("Entre com o valor maximo"))
resto = 0

if mini != maxi:

    print("os numeros divisiveis por 5 sao:")
    for i in range(mini,maxi+1):
        resto = i%5
        if resto == 0:
            print(i)
else:
    print("Minimo e maximo devem ser diferentes")

