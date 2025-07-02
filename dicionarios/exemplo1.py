q = int(input("Entre com a quantidade de alunos: "))
alunos  = []
for i in range(q):
    nome = input("Digite o nome do aluno: ")
    n1 = int(input("Digite n1: "))
    n2 = int(input("Digite n2: "))
    n3 = int(input("Digite n3: "))
    n4 = int(input("Digite n4: "))
    media  = (n1 + n2 + n3 + n4)/4
    if media < 6:
        situacao = "reprovado"
    else:
        situacao = "aprovado"
    aluno = {"nome": nome, "n1": n1, "n2": n2, "n3": n3,"n4": n4, "media": media, "situacao": situacao}
    alunos.append(aluno)
print("Notas dos alunos:")
print("-"*10)
for j in range(q):
    print(alunos[j].values())
