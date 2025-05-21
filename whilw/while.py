n = int(input("Entre com a qtt de notas: "))
i = 0
media = 0
total = 0

while i<n:
    valorNota = int(input("Entra com o valor de nota: "))
    total = total + valorNota
    i=i+1
media=total/n
print("A media eh: ", media)