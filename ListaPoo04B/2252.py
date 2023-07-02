k = 1
while True:
    try:
        N = int(input())
        v = list(map(float, input().split()))
        vOrdenado = []
        for n in v:
          vOrdenado.append(n)
        vOrdenado.sort(reverse = True)
        senha = ''
        for _ in range(N):
            senha+= str(v.index(vOrdenado[_]))
            v[v.index(vOrdenado[_])] = 1
        print(f"Caso {k}: {senha}")
        k+=1
    except EOFError:
        break
