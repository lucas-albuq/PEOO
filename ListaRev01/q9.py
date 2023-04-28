'''
9. Ler a quantidade de horas e minutos marcados em um relógio analógico e calcular o menor ângulo formado
entre os ponteiros do relógio. Mostrar uma mensagem de “Hora Inválida” se os valores fornecidos não formarem
uma hora válida.

Digite o horário no formato hh:mm
03:30

Menor ângulo entre os ponteiros = 75 graus
'''
h, m = map(int, input('Digite o horário no formato hh:mm \n').split(':'))
if h > 24 or m >= 60:
  print('Hora Inválida')
else:
  anguloM = m * 6
  anguloH = ((h * 60) + m) / 2
  total = anguloM - anguloH
  if total < 0:
    total *= -1
  if total > 180:
    total = 360 - total
  print(f'Menor ângulo entre os ponteiros = {total:.0f} graus')  
    
