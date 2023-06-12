n = []
num = int(input())
for x in range(10):
    n.append(num)
    num *= 2
    print(f'N[{x}] = {n[x]}')
