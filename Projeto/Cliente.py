import json


class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id  = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def set_id(self, nID):
    self.__id = nID
  def set_nome(self, nNome):
    self.__nome = nNome
  def set_email(self, nEmail):
    self.__email = nEmail
  def set_fone(self, nFone):
    self.__fone = nFone
  def get_id(self):
    return self.__id
  def get_nome(self):
    return self.__nome
  def get_email(self):
    return self.__email
  def get_fone(fone):
    return self.__fone

class NCliente:
  __clientes = []

  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id)
    cls.__clientes.append(obj)
    NCliente.salvar()

  @classmethod
  def listar(cls):
    NCliente.abrir()
    return cls.__clientes

  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None

  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
  
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)
    NCliente.salvar()
    
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", "r") as f:
        clientes_json = json.load(f)
        for obj in clientes_json:
          c = Cliente(obj["id"],
                     obj["nome"],
                     obj["email"],
                     obj["fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", "w") as f:
      json.dump(cls.__clientes, f, default=vars)
      