'''
6. Calcular o frete cobrado por uma transportadora para entregar uma carga com base na sua massa (peso) em
Kg e na distância percorrida até o destino em Km, utilizando a função Frete abaixo. O valor do frete deve ser de
um centavo de real para cada quilo transportado por quilometro.

def Frete(massa, distancia)
'''

def Frete(massa, distancia):
  frete = 0.01 * massa * distancia
  return frete

massa, distancia = map(int, input().split())
print(f'Frete = {Frete(massa, distancia)}')
