'''
3. Uma Viagem
Escrever a classe Viagem de acordo com o diagrama UML apresentado abaixo. A classe deve ter atributos para
armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. A classe deve possuir
método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto,
além dos métodos de acesso para definir e recuperar os atributos.
Escrever um programa para testar a classe.
'''
class Viagem:
  def __init__(self, distancia, tempo):
    self.set_distancia(distancia)
    self.set_tempo(tempo)
  def set_distancia(self, d):
    if v >= 0: self.__distancia = d
    else: raise ValueError()
  def set_tempo(self, t):
    if t >=0: self.__tempo = t
    else: raise ValueError()
  def get_distancia(self):
    return self.__distancia()
  def get_tempo(self):
    return self.__tempo()
  def velocidade_media(self):
    return self.__distancia/self.__set_tempo
class UI:
  @staticmethod
  def main():
    distancia = float(input('Digite a distância em KM: \n'))
    h, m = map(int, input('Digite o tempo de viagem no formato hh:mm').split(':'))
    tempo = (h*60 + m)/60
    x = Viagem(distancia, tempo)
    print(x.get_distancia())
    print(x.get_tempo())
    print(x.velocidade_media())
 UI.main()   
    
