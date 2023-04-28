'''
6. Ler três valores inteiros e calcular a soma do menor valor com o maior.

Digite três valores inteiros
2
1
3

A soma do maior com o menor número é 4.
'''

n1 = int(input('Digite três valores inteiros \n'))
n2 = int(input())
n3 = int(input())

sum = max(n1, n2, n3) + min(n1, n2, n3)

print(f'A soma do maior com o menor número é {sum}')
