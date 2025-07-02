entrada = input("Digite um número inteiro: ")

try:
    numero = int(entrada)
    print(f"Você digitou o número inteiro: {numero}")
except ValueError:
    print("Erro: A entrada não é um número inteiro válido.")
