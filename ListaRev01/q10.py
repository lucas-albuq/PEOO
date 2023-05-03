'''
10. Ler uma data no formato "dd/mm/aaaa" e verificar se é uma data válida, considerando como válidos os anos
entre 1900 e 2100, meses de 1 a 12 e dias de acordo com o mês.

Digite uma data no formato dd/mm/aaaa
32/08/2013

A data informada não é válida
'''
d, m, a = map(int, input('Digite uma data no formato dd/mm/aaaa \n').split('/'))

valAno = False
valDia = False
valMes = False

dias31 = [1, 3, 5, 7, 8, 10, 12]
dias30 = [4, 6, 9, 11]

if 1900 <= a <= 2100:
  valAno = True
if 1 <= m <= 12:
  valMes = True
if m in dias31:
  if 1 <= d <= 31:
    valDia = True
elif m in dias30:
  if 1 <= d <= 30:
    valDia = True
else:
  if 1 <= d <= 28:
    valDia = True
    
if valAno == valDia == valMes == True:
  print('A data informada é válida')
else:
  print('A data informada não é válida')
