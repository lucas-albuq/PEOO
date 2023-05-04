'''
4. Calcular o volume de uma esfera, dado o seu raio r, utilizando a função VolumeEsfera abaixo:

def VolumeEsfera(r)
'''
def VolumeEsfera(r):
  volume = 4/3 * 3.14 * r**3
  return volume

raio = int(input())
print(f'Volume = {VolumeEsfera(raio)}')
