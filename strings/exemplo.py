a = "quarta"
b =  "segunda"
c = []
tama, tamb= len(a), len(b)
maior = tama

if tama < tamb:
    maior = tamb

for i in range(maior):
    if i<tama:
        c.append(a[i])
    if i<tamb:
        c.append(b[i])
print("".join(c))

