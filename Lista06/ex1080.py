maior = 0
posicao = 0
for x in range(100):
    num = int(input())
    if num > maior:
        maior = num
        posicao = x + 1
print(maior)
print(posicao)
