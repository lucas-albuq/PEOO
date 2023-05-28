'''
4. Uma Entrada de Cinema
A classe deve ter atributos para armazenar o dia e o horário de uma sessão de cinema e métodos para calcular o
valor da entrada inteira e da meia-entrada.
O valor das entradas deve ser calculado com base nas seguintes regras:
• Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.
• Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.
• Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
• Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.
Escrever um programa para testar a classe.
'''

class Entrada:
  def __init__(self):
    self.dia = ''
    self.horario = 0
  def valorEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.dia.capitalize() == 'Quarta':
      return 8
    if self.dia.capitalize() in val1:
      if self.horario >= 17:
        return 24
      else:
        return 16
    if self.dia.capitalize() in val2:
      if self.horario>=17:
        return 30
      else:
        return 20
  def valorMeiaEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.dia.capitalize() == 'Quarta':
      return 8
    if self.dia.capitalize() in val1:
      if self.horario >= 17:
        return 12
      else:
        return 8
    if self.dia.capitalize() in val2:
      if self.horario>=17:
        return 15
      else:
        return 10

entrada = Entrada()
entrada.dia = input('Qual o dia da semana? \n')
entrada.horario, aux= map(int, input('Digite o horário em que deseja ir (hh:mm): \n').split(':'))
print(f'Você pagará R${entrada.valorEntrada()} em uma entrada.')
print(f'Você pagará R${entrada.valorMeiaEntrada()} em uma meia-entrada.')
