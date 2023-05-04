'''
3. Calcular a diagonal de um retângulo, dados a sua base b e sua altura h, utilizando a função Diagonal abaixo:

def Diagonal(b, h)
'''
def Diagonal(b, h):
  diagonal = (b**2 + h**2)**0.5
  return diagonal

b, h = map(int, input().split())
print(f'Diagonal = {Diagonal(b, h)}')
