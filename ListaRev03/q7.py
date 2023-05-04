'''
7. Obter o menor inteiro que seja maior ou igual ao número real x, utilizando a função MenorInteiro abaixo:

def MenorInteiro(x)
'''

def MenorInteiro(x):
  inteiro = round(x)
  if inteiro < x:
    inteiro +=1
  return inteiro

x = float(input())
print(f'O menor inteiro é {MenorInteiro(x)}')
  
