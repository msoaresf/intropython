frase = input("digite uma frase: ")
caracter = input("digite uma caracter: ")

def qttcaracter(frase,caracter):
    if caracter in frase:
        print(frase.count(caracter))

qttcaracter(frase,caracter)
