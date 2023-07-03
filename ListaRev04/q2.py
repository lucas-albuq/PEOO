class Esporte:
  def __init__(self, nome, horarios, mensalidade):
    self.__nome = nome
    self.__horarios = horarios
    self.__mensalidade = mensalidade
  def get_mensalidade(self):
    return self.__mensalidade
  def __str__(self):
    return f"\nNome - {self.__nome}\nHorários - {self.__horarios}\nMensalidade - R${self.__mensalidade}"
class Academia:
  def __init__(self, nome, endereco):
    self.__nome = nome
    self.__endereco = endereco
    self.__esportes = []
  def Inserir(self, e):
    self.__esportes.append(e)
  def Listar(self):
    return self.__esportes
  def mediaMensalidade(self):
    mensalidades = []
    for e in self.__esportes:
      mensalidades.append(e.get_mensalidade())
    media = sum(mensalidades) / len(self.__esportes)
    return media
class UI:
  @staticmethod
  def main():
    academia = Academia("infoweb", "rua lab4, bairro gilbert")
    op = int(input("3 - Inserir Esporte, 2 - Listar Esporte, 1 - Média das Mensalidades, 0 - Fim\n"))
    while op != 0:
      if op == 3:
        nome = input("Nome do esporte: ")
        horarios = input("Horários do esporte: ")
        mensalidade = float(input("Mensalidade do esporte: "))
        e = Esporte(nome, horarios, mensalidade)
        academia.Inserir(e)
      elif op == 2:
        print(*academia.Listar())
      elif op == 1:
        print(f"{academia.mediaMensalidade():.2f}")
      op = int(input("3 - Inserir Esporte, 2 - Listar Esporte, 1 - Média das Mensalidades, 0 - Fim\n"))
UI.main()
