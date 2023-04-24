'''
1. Ler dois valores inteiros e imprimir o maior deles, ou a mensagem "Números iguais", se forem iguais.

Digite dois valores inteiros
1
2
Maior = 2
'''
print('Digite dois valores inteiros')
n1 = int(input())
n2 = int(input())

if n1 == n2:
  print('Números iguais')
else:
  print(f'Maior = {max(n1, n2)}')
