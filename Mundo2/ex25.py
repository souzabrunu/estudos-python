n = int(input())

# Inicializa o dicionario para armazenar toneladas por pais
exportacoes = {}

# Loop para ler os dados de cada exportacao
for _ in range(n):
    linha = input().strip()
    pais, toneladas = linha.split(",")
    pais = pais.strip()
    toneladas = float(toneladas.strip())
    if pais in exportacoes:
      exportacoes[pais] += toneladas
    else:
      exportacoes[pais] = toneladas

for pais, total in exportacoes.items():
  if total.is_integer():
    total = int(total)
    print(f"{pais}: {total} toneladas")
