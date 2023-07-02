#INCOMPLETO DEVIDO A PROBLEMAS DE RECURSIVIDADE!!!(ainda vou ajeitar)

class Cliente:
  def __init__(self, nome, cpf, limite):
    self.__nome = nome
    self.__cpf = cpf
    self.__limite = limite
    self.__socio = None
  def SetSocio(self, c):
    if self.__socio == None:
      self.__socio = c
      self.__socio.SetSocio(self)
  def GetLimite(self):
    if self.__socio != None:
      return self.__limite + self.__socio.GetLimite()
    return self.__limite
  def __str__(self):
    return f'Nome - {self.__nome}\nCPF - {self.__cpf}\nLimite - {self.__limite}\nSocio - {self.__socio}'
class Empresa:
  def __init__(self):
    self.__clientes = []
  def Inserir(self, c):
    self.__clientes.append(c)
  def Listar(self):
    return self.__clientes

class UI:
  @staticmethod
  def main():
    op = int(input("1 - Inserir cliente, 2 - Listar clientes 3- Fim\n"))
    empresa = Empresa()
    while op != 3:
      if op == 1:
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        limite = float(input("Insira o limite do cliente: "))
        c = Cliente(nome, cpf, limite)
        empresa.Inserir(c)
        op2 = input("Deseja inserir um sócio?(S/N)\n").upper()
        if op2 == 'S':
          nome = input("Nome do cliente: ")
          cpf = input("CPF do cliente: ")
          limite = float(input("Insira o limite do cliente: "))
          c2 = Cliente(nome, cpf, limite)
          empresa.Inserir(c2)
          c.SetSocio(c2)

        op3 = input("\nDeseja ver o limite dos clientes? (S/N)\n").upper()
        if op3 == 'S':
          print(c.GetLimite())
      elif op == 2:
        print(*empresa.Listar())
      op = int(input("1 - Inserir cliente, 2 - Listar clientes 3- Fim\n"))
UI.main()
