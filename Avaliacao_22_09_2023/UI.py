from compromisso import Compromisso, NCompromisso


class UI:

  @classmethod
  def Main(cls):
   op = 0
   while (op != 99):
       op = UI.Menu()
       if op == 1: UI.CompromissoInserir()
       if op == 2: UI.CompromissoListar()
       if op == 3: UI.CompromissoAtualizar()
       if op == 4: UI.CompromissoExcluir()
       if op == 5: UI.Compromissos_do_Mes()

  @classmethod
  def Menu(cls):
     print("\nCompromissos")
     print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Compromissos do Mes")
     print("\nSair")
     print("99-Sair")
     return int(input())
     
  @classmethod
  def CompromissoInserir(cls):
    assunto = input("Assunto: ")
    local = input("Local: ")
    data = input("Data (dd/mm/yyyy): ")
    compromisso = Compromisso(0, assunto, local, data)
    NCompromisso.inserir(compromisso)

  @classmethod
  def CompromissoListar(cls):
    for compromisso in NCompromisso.listar():
      print(compromisso)

  @classmethod
  def CompromissoAtualizar(cls):
    print("Compromissos cadastrados")
    UI.CompromissoListar()
    id = int(input("Informe o id para atualizar: "))
    assunto = input("Assunto: ")
    local = input("Local: ")
    data = input("Data (dd/mm/yyyy): ")
    compromisso = Compromisso(id, assunto, local, data)
    NCompromisso.atualizar(compromisso)

  @classmethod
  def CompromissoExcluir(cls):
    print("Compromissos cadastrados")
    UI.CompromissoListar()
    id = int(input("Informe o id para excluir: "))
    compromisso = Compromisso(id, "", "", "")
    NCompromisso.excluir(compromisso)
  
  @classmethod
  def Compromissos_do_Mes(cls):
    print(*NCompromisso.Comps_do_Mes())

UI.Main()
