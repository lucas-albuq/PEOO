'''
I. Implementar classes em Python para representar:

1. Um Círculo
A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua
circunferência.
Escrever um programa para testar a classe.
'''
import math
class Circulo:
  def __init__(self):
    self.raio = 0
  def calc_Area(self):
    return math.pi * self.raio**2
  def calc_Circ(self):
    return 2 * math.pi * self.raio
 
x = Circulo()
print("Digite o raio do círculo:")
x.raio = float(input())

print(f"Area = {x.calc_Area()} \nCircunferência = {x.calc_Circ()}")
