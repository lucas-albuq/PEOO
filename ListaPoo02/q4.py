'''
4. Uma Entrada de Cinema
Escrever uma classe para modelar uma entrada de cinema com todos os atributos encapsulados. A classe deve ter
atributos para armazenar o dia e o horário de uma sessão de cinema e métodos para calcular o valor da entrada
inteira e da meia-entrada, além dos métodos de acesso para definir e recuperar os atributos.
O valor das entradas deve ser calculado com base nas seguintes regras:
• Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.
• Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.
• Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
• Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.
Escrever um programa para testar a classe e elaborar seu digrama UML.
'''
class Entrada:
  def __init__(self, dia, horario):
    self.set_dia(dia)
    self.set_horario(horario)
  def set_dia(self, v):
    self.__dia = v
  def set_horario(self, v):
    if v >= 0: self.__horario = v
  def get_dia(self):
    return self.__dia
  def get_horario(self):
    return self.__horario
  def valorEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.__dia.capitalize() == 'Quarta':
      return 8
    if self.__dia.capitalize() in val1:
      if self.__horario >= 17:
        return 24
      else:
        return 16
    if self.__dia.capitalize() in val2:
      if self.__horario>=17:
        return 30
      else:
        return 20
  def valorMeiaEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.__dia.capitalize() == 'Quarta':
      return 8
    if self.__dia.capitalize() in val1:
      if self.__horario >= 17:
        return 12
      else:
        return 8
    if self.__dia.capitalize() in val2:
      if self.__horario>=17:
        return 15
      else:
        return 10
class UI:
  @staticmethod
  class main():
    dia = input('Qual o dia da semana? \n')
    horario, aux = map(int, input('Digite o horário em que deseja ir (hh:mm): \n').split(':'))
    entrada = Entrada(dia, horario)

    print(f'Você pagará R${entrada.valorEntrada()} em uma entrada.')
    print(f'Você pagará R${entrada.valorMeiaEntrada()} em uma meia-entrada.')
UI.main()    
  
