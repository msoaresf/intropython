"""Considere um registro que deve armazenar os dados referentes ao código (inteiro) de um produto de uma empresa que fabrica peças de vestuário, o tipo
do produto (tipos disponíveis: P, M e G – pequeno, médio e grande), a quantidade vendida
para cada um dos 6 dias de uma semana (estrutura que armazena 6 elementos, inteiros) e a
quantidade média vendida na semana (média dos 6 dias). Considere que os dados relativos
aos 20 produtos vendidos pela empresa são armazenados em uma lista cujos elementos correspondem a essa estrutura. Faça um programa que processe as vendas efetuadas, armazenando
os dados correspondentes na estrutura mencionada para 6 dias de uma semana. O programa
deverá ler dados referentes ao dia da semana, código de produto e quantidade vendida desse
produto. No final da entrada dos dados da semana, o programa principal deverá calcular as
médias da semana para cada produto e imprimir um relatório com os dados finais da estrutura:
para cada produto, total vendido por dia e a média da semana.
"""
produto = {
    "codigo": 123,
    "tipo": "M",
    "vendas": [0, 0, 0, 0, 0, 0],
    "media": 0.0
}
NUM_PRODUTOS = 20
NUM_DIAS = 6

# Lista para armazenar os 20 produtos
produtos = []

# Passo 1: Cadastro inicial dos produtos
print("Cadastro dos produtos:")
for i in range(NUM_PRODUTOS):
    print(f"\nProduto {i+1}")
    codigo = int(input("Digite o código do produto: "))
    tipo = input("Digite o tipo do produto (P, M ou G): ").upper()
    while tipo not in ["P", "M", "G"]:
        tipo = input("Tipo inválido! Digite P, M ou G: ").upper()
    vendas = [0] * NUM_DIAS  # Inicializa com 0 vendas para os 6 dias
    produtos.append({
        "codigo": codigo,
        "tipo": tipo,
        "vendas": vendas,
        "media": 0.0
    })

# Passo 2: Entrada de vendas
print("\nDigite os dados de venda da semana. Digite -1 para parar.")
while True:
    codigo = int(input("\nCódigo do produto (ou -1 para encerrar): "))
    if codigo == -1:
        break
    dia = int(input("Dia da semana (1 a 6): "))
    while dia < 1 or dia > 6:
        dia = int(input("Dia inválido. Digite de 1 a 6: "))
    qtd = int(input("Quantidade vendida: "))

    # Localiza o produto pelo código
    encontrado = False
    for produto in produtos:
        if produto["codigo"] == codigo:
            produto["vendas"][dia - 1] += qtd  # dia-1 porque lista começa no 0
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")

# Passo 3: Calcula médias
for produto in produtos:
    total = sum(produto["vendas"])
    produto["media"] = total / NUM_DIAS

# Passo 4: Relatório final
print("\nRELATÓRIO FINAL")
for produto in produtos:
    print(f"\nCódigo: {produto['codigo']}, Tipo: {produto['tipo']}")
    print("Vendas por dia:", produto["vendas"])
    print(f"Média semanal: {produto['media']:.2f}")
