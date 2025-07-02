palavra = input("Digite uma palavra: ")

# Remove espaços e transforma tudo em minúsculo (opcional)
palavra = palavra.replace(" ", "").lower()

# Cria um conjunto com as letras da palavra
letras_diferentes = set(palavra)

# Mostra o total de letras únicas
print(f"A palavra contém {len(letras_diferentes)} letras diferentes.")
