import json
import datetime


class Compromisso:
    def __init__(self, id, assunto, local, data):
      self.__id = id
      self.__assunto = assunto
      self.__local = local
      self.__data = data

    def __str__(self):
        return f'{self.__id} - {self.__assunto} - {self.__local} - {self.__data}'
    
    def get_id(self):
        return self.__id
        
    def get_assunto(self):
        return self.__assunto

    def get_local(self):
        return self.__local

    def get_data(self):
        return self.__data
    
    def set_id(self, id):
        self.__id = id

    def set_assunto(self, assunto):
        self.__assunto = assunto

    def set_local(self, local):
        self.__local = local

    def set_data(self, data):
        self.__data = data

class NCompromisso:
  __compromissos = []

  @classmethod
  def inserir(cls, obj):
    NCompromisso.abrir()
    id = 0
    for c in cls.__compromissos:
      if c.get_id() > id: id = c.get_id()
    obj.set_id(id+1)
    cls.__compromissos.append(obj)
    NCompromisso.salvar()

  @classmethod
  def listar(cls):
    NCompromisso.abrir()
    return cls.__compromissos

  @classmethod
  def listar_id(cls, id):
    NCompromisso.abrir()
    for c in cls.__compromissos:
      if c.get_id() == id: return c
    return None

  @classmethod
  def atualizar(cls, obj):
    NCompromisso.abrir()
    compromisso = NCompromisso.listar_id(obj.get_id())
    if compromisso != None:
      compromisso.set_assunto(obj.get_assunto())
      compromisso.set_local(obj.get_local())
      compromisso.set_data(obj.get_data())
      NCompromisso.salvar()

  @classmethod
  def excluir(cls, obj):
    NCompromisso.abrir()
    compromisso = NCompromisso.listar_id(obj.get_id())
    cls.__compromissos.remove(compromisso)
    NCompromisso.salvar()
  
  @classmethod
  def abrir(cls):
    try:
      cls.__compromissos = []
      with open("compromissos.json", "r") as c:
        compromissos_json = json.load(c)
        for compromisso in compromissos_json:
          c = Compromisso(compromisso["_Compromisso__id"], 
                          compromisso["_Compromisso__assunto"],
                          compromisso["_Compromisso__local"], 
                          compromisso["_Compromisso__data"])
          cls.__compromissos.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("compromissos.json", "w") as c:
      json.dump(cls.__compromissos, c, default=vars)

  @classmethod
  def Comps_do_Mes(cls):
    NCompromisso.abrir()
    lista_mes_atual = []
    hoje = datetime.datetime.now()
    for c in cls.__compromissos:
      data_c = datetime.datetime.strptime(c.get_data(), "%d/%m/%Y")
      if (data_c.month == hoje.month) and (data_c.year == hoje.year):
        lista_mes_atual.append(c)
    if lista_mes_atual == []:
      return "Nenhum compromisso no mês atual"
    else:
      return lista_mes_atual
