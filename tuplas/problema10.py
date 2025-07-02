"""Montar um conjunto de dados em que cada registro contém o resultado de uma enquete do Ibope sobre a audiência de canais de TV durante o dia. Para cada entrevista realizada devem ser armazenados a idade, o sexo, o estado civil e o grau de instrução da pessoa entrevistada, o horário em que foi feita a entrevista e o canal a que está assistindo. Entrar com os dados pelo teclado e imprimir:
1. o canal de maior audiência, sem considerar o horário;
2. o canal de maior audiência no horário compreendido entre 20 e 21 horas;
3. idade, sexo, estado civil e grau de intrução dos entrevistados que estavam assistindo ao
canal de maior audiência naquele horário;
4. o horário de menor audiência entre as mulheres;
5. idade média dos que preferem o canal 12 entre 10 e 12 horas.
{
    "idade": 25,
    "sexo": "F",
    "estado_civil": "Solteira",
    "instrucao": "Superior completo",
    "horario": 20,
    "canal": 12
}
"""
entrevistas = []

print(">>> ENTRADA DE DADOS (digite -1 na idade para encerrar) <<<")
while True:
    idade = int(input("Idade: "))
    if idade == -1:
        break
    sexo = input("Sexo (M/F): ").strip().upper()
    estado_civil = input("Estado civil: ").strip().capitalize()
    instrucao = input("Grau de instrução: ").strip().capitalize()
    horario = int(input("Horário da entrevista (0 a 23): "))
    canal = int(input("Canal que está assistindo: "))

    entrevistas.append({
        "idade": idade,
        "sexo": sexo,
        "estado_civil": estado_civil,
        "instrucao": instrucao,
        "horario": horario,
        "canal": canal
    })

# -------------------------
# 1. Canal de maior audiência (geral)
# -------------------------
from collections import Counter

todos_os_canais = [e["canal"] for e in entrevistas]
contagem_geral = Counter(todos_os_canais)
canal_mais_geral = contagem_geral.most_common(1)[0][0]

print("\n1. Canal de maior audiência (geral):", canal_mais_geral)

# -------------------------
# 2. Canal de maior audiência entre 20 e 21h
# -------------------------
entre_20_21 = [e for e in entrevistas if e["horario"] == 20]
canais_20_21 = [e["canal"] for e in entre_20_21]
if canais_20_21:
    canal_mais_20_21 = Counter(canais_20_21).most_common(1)[0][0]
    print("2. Canal de maior audiência entre 20h e 21h:", canal_mais_20_21)
else:
    print("2. Nenhuma entrevista registrada entre 20h e 21h.")

# -------------------------
# 3. Dados dos que assistiram esse canal entre 20h e 21h
# -------------------------
print("\n3. Dados dos entrevistados que assistiram ao canal", canal_mais_20_21, "entre 20h e 21h:")
for e in entre_20_21:
    if e["canal"] == canal_mais_20_21:
        print(f"Idade: {e['idade']}, Sexo: {e['sexo']}, Estado civil: {e['estado_civil']}, Instrução: {e['instrucao']}")

# -------------------------
# 4. Horário de menor audiência entre mulheres
# -------------------------
horarios_mulheres = [e["horario"] for e in entrevistas if e["sexo"] == "F"]
if horarios_mulheres:
    contagem_horas_femininas = Counter(horarios_mulheres)
    horario_menor_feminino = contagem_horas_femininas.most_common()[-1][0]
    print("\n4. Horário de menor audiência entre mulheres:", horario_menor_feminino, "h")
else:
    print("\n4. Nenhuma mulher foi entrevistada.")

# -------------------------
# 5. Idade média dos que assistem canal 12 entre 10h e 12h
# -------------------------
canal12_10_12 = [e for e in entrevistas if 10 <= e["horario"] <= 12 and e["canal"] == 12]
if canal12_10_12:
    media_idade = sum(e["idade"] for e in canal12_10_12) / len(canal12_10_12)
    print("\n5. Idade média dos que assistem canal 12 entre 10h e 12h:", round(media_idade, 2))
else:
    print("\n5. Ninguém assistia o canal 12 entre 10h e 12h.")

