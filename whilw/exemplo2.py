n=1
qtt=0
while n>0:
    n = int(input("Entre com um numero: "))
    resto = n%2
    if resto == 0:
        qtt = qtt+1
        print("O numero {} é par".format(n))
print("foram informados {} numeros pares".format(qtt))