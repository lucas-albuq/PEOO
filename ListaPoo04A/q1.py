import random

class Bingo:
  def __init__(self):
    self.__numBolas = 0
    self.__sorteados = []

  def Iniciar(self, numBolas):
    if numBolas > 0: self.__numBolas = numBolas
    else: raise ValueError("Número inválido")

  def Proximo(self):
    if len(self.__sorteados) == self.__numBolas:
        return -1  # Todas as bolas já foram sorteadas
    else:
      bola_sorteada = random.randint(1, self.__numBolas)
      while bola_sorteada in self.__sorteados: #While para impedir o mesmo número de ser sorteado duas vezes
        bola_sorteada = random.randint(1, self.__numBolas)
      self.__sorteados.append(bola_sorteada)
      return bola_sorteada

  def Sorteados(self):
    return self.__sorteados
class UI:
  def main():
    jogo = Bingo()
    n = int(input("Digite o número de bolas: \n"))
    jogo.Iniciar(n)
    for _ in range(n):
        print(f'Bola sorteada - {jogo.Proximo()}') 
    print(f'Bolas sorteadas - {jogo.Sorteados()}')
UI.main()
