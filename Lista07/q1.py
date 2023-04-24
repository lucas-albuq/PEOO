'''
1. Retornar o maior entre dois números, usando a função Maior abaixo. O programa deve solicitar do usuário dois
valores e mostrar o maior valor entre eles utilizando a função Maior, que deve ser também implementada.

def maior(x, y)
'''

def maior(x, y):
  maior = x
  if y > x:
    maior = y
  return maior

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

print(f'O maior é {maior(x, y)}')
