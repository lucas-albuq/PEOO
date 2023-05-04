'''
5. Calcular o volume em litros de uma caixa d ́água (no formato de paralelepípedo), dados sua altura h, largura l e
profundidade p, em metros, utilizando a função VolumeLitros abaixo:

def VolumeLitros(h, l, p)
'''

def VolumeLitros(h, l, p):
  volumeMetroCubico = h * l * p
  volumeLitros = volumeMetroCubico * 1000
  return volumeLitros

h, l, p = map(float, input().split())
print(f'Volume em Litros = {VolumeLitros(h, l, p)}')
