termo = int(input("Entre com o numer"))
razao = int(input("Entre com o razao"))
qtt = int(input("Entre com o qtt"))
resultado =[]
resultado.append(termo)

for i in range(qtt):
    termo = termo + razao
    resultado.append(termo)
print(resultado)