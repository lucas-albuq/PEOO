lista = []
for x in range(10):
    i = int(input())
    lista.append(i)
for y in range(10):
    if lista[y] <= 0:
        print(f'X[{y}] = 1')
    else:
        print(f'X[{y}] = {lista[y]}')
