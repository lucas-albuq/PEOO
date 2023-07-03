class Jogador:
  def __init__(self, nome, camisa, gols):
    self.__nome = nome
    self.__camisa = camisa
    self.__gols = gols
  def get_Gols(self):
    return self.__gols
  def __str__(self):
    return f"Nome - {self.__nome}\nCamisa - {self.__camisa}\nGols - {self.__gols}"
class Time:
  def __init__(self, nome, estado):
    self.__nome = nome
    self.__estado = estado
    self.__jogadores = []
  def Inserir(self, j):
    self.__jogadores.append(j)
  def Listar(self):
    return self.__jogadores
  def Artilheiro(self):
    maiorGols = 0
    artilheiro = 0
    for j in self.__jogadores:
      if j.get_Gols() > maiorGols:
        maiorGols = j.get_Gols()
        artilheiro = self.__jogadores.index(j)
    return self.__jogadores[artilheiro]
class UI:
  @staticmethod
  def main():
    time = Time("infoweb", "RN")
    op = int(input("1 - Inserir Jogador, 0 - Fim\n"))
    while op != 0:
      if op == 1:
        nome = input("Nome do jogador: ")
        camisa = int(input("Camisa do jogador: "))
        gols = int(input("Quantidade de gols: "))
        j = Jogador(nome, camisa, gols)
        time.Inserir(j)
      elif op == 2:
        print(time.Artilheiro())
      op = int(input("2 - Ver artilheiro, 1 - Inserir Jogador, 0 - Fim\n"))
UI.main()
