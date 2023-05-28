'''
1. Um Círculo
Escrever a classe Círculo de acordo com o diagrama UML apresentado abaixo. A classe deve ter um atributo raio
para armazenar a dimensão da figura e métodos para calcular sua área e sua circunferência, além dos métodos de
acesso para definir e recuperar o atributo raio.
Escrever um programa para testar a classe.
'''
from math import pi
class Circulo:
  def __init__(self, raio):
    self.__raio = 0.0
    self.set_raio(raio)
  def set_raio(self, v):
    if v >= 0: self.__raio = v
    else: raise ValueError()
  def get_raio(self):
    return self.__raio
  def calc_area(self):
    return pi*self.__raio**2
  def calc_circunferencia(self):
    return 2*pi*self.__raio
class UI:
  @staticmethod
  def main():
    x = Circulo(float(input('Digite o valor do raio do círculo: \n')))
    print(x.get_raio())
    print(x.calc_area())
    print(x.calc_circunferencia())
   
    x.set_raio(float(input('Digite o novo valor do raio do círculo: \n')))
    print(x.get_raio())
    print(x.calc_area())
    print(x.calc_circunferencia())
UI.main()    
