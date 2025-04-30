a = int (input("Entra com o valor de a: "))
b = int (input("Entra com o valor de b: "))
c = int (input("Entra com o valor de c: "))

print("O que deseja fazer:")
print("1- media aritimetica")
print("2- media harmonica")
print("3- media ponderada")
o = int (input("Qual op: "))

match o:
    case 1:
        mediaA = (a + b + c)/3
        print("A media é:", mediaA)
    case 2:
        mediaH = 3/ ((1/a)+(1/b)+(1/c))
        print("A media é:", mediaH)
    case 3:
        mediaP = ((1*a) + (2*b) + (3*c)) / (1 + 2 + 3)
        print("A media é:", mediaP)
