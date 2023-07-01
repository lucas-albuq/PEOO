N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

def calcula_distancia(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5

for _ in range(N):
    menor_distancia = float("inf")
    for j  in range(N):
        if a[_] != a[j]:
            distancia = calcula_distancia(a[_][0], a[_][1], a[_][2], a[j][0], a[j][1], a[j][2])
            menor_distancia = min(distancia, menor_distancia)
    if menor_distancia <= 20: print("A")
    elif menor_distancia <= 50: print("M")
    else: print("B")
