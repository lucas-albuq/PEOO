qtd = int(input())
num = list(map(int, input().split()))
menor = min(num)
for x in range(qtd):
    if num[x] == menor:
        pos = x
        break
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')
