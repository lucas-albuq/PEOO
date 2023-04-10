N = int(input())
total = 0
c = 0
r = 0
s = 0
for x in range(N):
    quan, tipo = input().split()
    if tipo == 'C':
        c += int(quan)
        total += int(quan)
    elif tipo == 'R':
        r += int(quan)
        total += int(quan)
    elif tipo == 'S':
        s += int(quan)
        total += int(quan)
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {c/total * 100:.2f} %')
print(f'Percentual de ratos: {r/total * 100:.2f} %')
print(f'Percentual de sapos: {s/total * 100:.2f} %')
