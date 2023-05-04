'''
18. Ordenar e mostrar três valores em ordem crescente (sem utilizar o sort)

def MostrarOrdenado(a, b, c)
'''

def MostrarOrdenado(a, b, c):
  ordem = []
  ordem.append(str(min(a, b, c)))
  ordem.append(str(max(a, b, c)))
  if str(a) not in ordem:
    ordem.insert(1, str(a))
  elif str(b) not in ordem:
    ordem.insert(1, str(b))
  elif str(c) not in ordem:
    ordem.insert(1, str(c))
  resposta = ', '.join(ordem)  
  return resposta

a, b, c = map(int, input().split())
print(MostrarOrdenado(a, b, c))
