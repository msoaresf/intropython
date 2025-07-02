agenda = {}

while True:
    nome = input('Digite o nome do contato: ')
    if nome == "":
        break
    idade = int(input('Digite a idade do contato: '))
    numero = input('Digite o numero do contato: ')
    agenda[nome] = {'idade': idade, 'numero': numero}

print("-"*30)
print("Em oidem alfabetica: ")
print("Nome | Idade | Numero: ")
for nome in sorted(agenda):
    dados = agenda[nome]
    print("{} | {} | {}".format(nome, dados['idade'], dados['numero']))
