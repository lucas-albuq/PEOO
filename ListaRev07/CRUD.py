class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def get_id(self):
    return self.__id
  def get_nome(self):
    return self.__nome
  def get_email(self):
    return self.__email
  def get_fone(self):
    return self.__fone
  def set_nome(self, n):
    self.__nome = n
  def set_email(self, e):
    self.__email = e
  def set_fone(self, f):
    self.__fone = f
  def __str__(self):
    return f"Cliente {self.__id} - {self.__nome}\nEmail - {self.__email}\nTelefone - {self.__fone}\n"
class NCliente:
  @classmethod
  def __init__(self):
    self.__clientes = []
  def Inserir(self, obj):
    self.__clientes.append(obj)
  def Listar(self):
    return self.__clientes
  def Listar_id(self, id):
    for cliente in self.__clientes:
      if cliente.get_id() == id:
        return cliente
  def Atualizar(self, obj):
    self.Excluir(self.Listar_id(obj.get_id()))
    self.Inserir(obj)
  def Excluir(self, obj):
    self.__clientes.remove(obj)
class UI:
  @staticmethod
  def Menu():
    print("0 - Fim, 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
    return int(input())
  @staticmethod
  def main():
    op = UI.Menu()
    listaClientes = NCliente()
    while op != 0:
      if op == 1:
        id = int(input('id: '))
        nome = input('nome: ')
        email = input('email: ')
        fone = input('fone: ')
        cliente = Cliente(id, nome, email, fone)
        listaClientes.Inserir(cliente)
      elif op == 2:
        print(*listaClientes.Listar())
      elif op == 3:
        id = int(input('id do cliente: '))
        nome = input('Novo nome: ')
        email = input('Novo email: ')
        fone = input('Novo fone: ')
        cliente = Cliente(id, nome, email, fone)
        listaClientes.Atualizar(cliente)
      elif op == 4:
        id = int(input('id do cliente: '))
        listaClientes.Excluir(listaClientes.Listar_id(id))
      op = UI.Menu()
UI.main()
    
