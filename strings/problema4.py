# Lê a string
texto = input("Digite uma string: ")

# Lê o caractere a ser buscado
caractere = input("Digite o caractere que deseja encontrar: ")

# Garante que o usuário digitou apenas um caractere
if len(caractere) != 1:
    print("Por favor, digite apenas um único caractere.")
else:
    posicao = texto.rfind(caractere)

    if posicao == -1:
        print(f"O caractere '{caractere}' não foi encontrado na string.")
    else:
        print(f"A última ocorrência do caractere '{caractere}' está na posição {posicao}.")
