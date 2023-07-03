from datetime import datetime
class Paciente:
  def __init__(self, n, c, t, nasc):
    self.__nome = n
    self.__cpf = c
    self.__telefone = t
    self.__nascimento = nasc
  def Idade(self):
    data_atual = datetime.now()
    delta = data_atual - self.__nascimento
    return delta.days//365
  def __str__(self):
    return f"Nome - {self.__nome}\nCPF - {self.__cpf}\nTelefone - {self.__telefone}\nNascimento - {self.__nascimento}"
class UI:
  @staticmethod
  def main():
    nome = input("Nome do paciente: ")
    cpf = input("CPF do paciente: ")
    telefone = input("Telefone do paciente: ")
    nascimento = input("Nascimento do paciente(dd/mm/yyyy): ")
    nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    paciente = Paciente(nome, cpf, telefone, nascimento)
    print(f"Idade do paciente: {paciente.Idade()} anos")
UI.main()
