'''
2. Retornar o maior entre três números, usando a função Maior abaixo. O programa deve solicitar do usuário três
valores e mostrar o maior entre eles utilizando a função Maior, que deve ser também implementado.

def maior(x, y, z)
'''

def maior(x, y, z):
  maior = x
  if y > maior:
    maior = y
  if z > maior:
    maior = z
  return maior

x = int(input('Digite um número:'))
y = int(input('Digite outro número:'))
z = int(input('Digite mais um número:'))

print(f'O maior número é {maior(x, y, z)}')
