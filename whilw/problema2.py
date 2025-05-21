n = int(input("Entre com N "))
soma = 0
i = 0
while i<n:
   nreais = int(input("Entra com o valor para n: "))
   if nreais > 0:
       soma = soma + nreais
       i = i+1
print("soma dos reais positivos: ", soma)