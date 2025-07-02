#somar duas matriz
m1= [[1,2],[3,4]]
m2= [[5,6],[7,8]]
m3 =[]

for i in range (2):
    soma =[]
    for j in range (2):
        m1m2 =m1[i][j]+m2[i][j]
        soma.append(m1m2)
    m3.append(soma)
for i in range (2):
    print(m3[i])