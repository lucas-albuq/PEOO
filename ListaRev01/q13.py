'''13. Ler 10 números inteiros em uma única linha separados por espaço, mostrar o maior e o menor número.

Digite dez valores inteiros
1 2 3 4 5 6 7 8 9 10

O maior valor é 10 e o menor é 1
'''

num = list(map(int, input('Digite dez valores inteiros \n').split()))
print(f'O maior valor é {max(num)} e o menor é {min(num)}')
