'''
15. Ler três valores e mostrar em ordem crescente

Digite três valores:
10
2
15

2, 10, 15
'''

print('Digite três valores:')
a = int(input())
b = int(input())
c = int(input())

valores = [a, b, c]
valores.sort()

print(f'{valores[0]}, {valores[1]}, {valores[2]}')
