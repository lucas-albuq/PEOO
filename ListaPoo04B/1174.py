v = []
for x in range(100):
    n = float(input())
    v.append(n)
    if v[x] <= 10:
        print(f'A[{x}] = {v[x]}')
