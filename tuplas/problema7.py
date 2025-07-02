""". Defina um dicionário que tenha dois campos. O primeiro
campo contém uma string. O segundo campo – do tipo tupla – é formado por três outros
campos, todos inteiros. Faça um programa que:
• preencha cada um dos campos dessa variável por leitura;
• imprima os valores contidos em todos os campos;
• substitua o conteúdo do segundo campo por leitura;
• imprima os valores finais em cada campo.
"""
# Criação do dicionário vazio
dado = {}

# Leitura do primeiro campo (string)
dado["texto"] = input("Digite uma string: ")

# Leitura dos três inteiros para a tupla
print("Digite três números inteiros:")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
dado["valores"] = (n1, n2, n3)

# Exibe os valores atuais
print("\nValores armazenados:")
print("Texto:", dado["texto"])
print("Tupla de valores:", dado["valores"])

# Substituição da tupla por novos valores
print("\nSubstitua agora os três números inteiros:")
n1 = int(input("Novo primeiro número: "))
n2 = int(input("Novo segundo número: "))
n3 = int(input("Novo terceiro número: "))
dado["valores"] = (n1, n2, n3)

# Exibe os valores finais
print("\nValores finais:")
print("Texto:", dado["texto"])
print("Tupla de valores atualizada:", dado["valores"])
