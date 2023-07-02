J, R = map(int, input().split())
rodadas = list(map(int, input().split()))
pontos = [0] * J
for _ in range(J):
    pontos[_] += sum(rodadas[_::J])
pontos = pontos[::-1]
vencedor = J - pontos.index(max(pontos))
print(vencedor)
