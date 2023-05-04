'''
14. Obter o último dia de um mês/ano no formato "dd/mm/aaaa", utilizando a função UltimoDia abaixo:
def UltimoDia(mes, ano)
'''

'''
14. Obter o último dia de um mês/ano no formato "dd/mm/aaaa", utilizando a função UltimoDia abaixo:
def UltimoDia(mes, ano)
'''

def UltimoDia(mes, ano):
  if ano % 4 == 0:
    anoBissexto = True
  else: 
    anoBissexto = False
  if mes < 10:
    strMes = '0'+str (mes)
  else:
    strMes = str(mes)
  diasPorMes= {1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}  
  if anoBissexto == True and mes == 2:
    data = ['29', strMes, str(ano)]
    resposta = '/'.join(data)
  else:
    data = [str(diasPorMes[mes]), strMes, str(ano)]
    resposta = '/'.join(data)
  return resposta

mes = int(input())
ano = int(input())

print(UltimoDia(mes, ano))
   
