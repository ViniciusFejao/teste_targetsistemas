import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma = 0
dias_com_faturamento = 0

for registro in dados:
    valor = registro['valor']
    if valor > 0:
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor
        soma += valor
        dias_com_faturamento += 1

media_mensal = soma / dias_com_faturamento if dias_com_faturamento > 0 else 0
dias_acima_media = sum(1 for registro in dados if registro['valor'] > media_mensal)

print("Menor faturamento: ", menor_faturamento)
print("Maior faturamento: ", maior_faturamento)
print("Dias com faturamento acima da média ", dias_acima_media)