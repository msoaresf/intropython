entrada = input("Digite três números separados por espaço: ")

# Divide a string em uma lista de strings
valores = entrada.split()

# Converte para inteiros e carrega em A, B e C
A, B, C = int(valores[0]), int(valores[1]), int(valores[2])

# Mostra os valores
print("A:", A)
print("B:", B)
print("C:", C)
