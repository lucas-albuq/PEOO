'''
I. Implementar classes em Python para representar:

3. Uma Viagem
A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem
realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo
com a distância e o tempo gasto.
Escrever um programa para testar a classe.
'''

class Viagem:
  def __init__(self):
    self.dist = 0
    self.horas = 0
    self.minutos = 0
  def calc_velMedia(self):
    return self.dist/((self.horas*60 + self.minutos)/60)
  
