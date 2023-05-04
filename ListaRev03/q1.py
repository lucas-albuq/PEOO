'''
1. Retornar o menor entre dois números, utilizando a função Menor abaixo:

def Menor(x, y)
'''
def Menor(x, y):
  menor = min(x, y)
  return menor

a, b = map(int, input().split())
print(f'Menor = {Menor(a, b)}')
