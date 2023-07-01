operacao = input()

num_linhas = 12
num_colunas = 12

matriz = []
for k in range(num_linhas):
  matriz.append([0] * num_colunas)

for k in range(num_linhas):
    for y in range(num_colunas):
        matriz[k][y] = float(input())
soma = 0
qtd = 0
for k in range(num_linhas):
    for y in range(num_colunas):
        if y > k:
            soma += matriz[k][y]
            qtd += 1
if operacao == 'S':
    print(f"{soma:.1f}")
else: print(f"{soma/qtd:.1f}")
