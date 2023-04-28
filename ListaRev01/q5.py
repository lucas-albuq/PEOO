'''
5. Ler o número do mês (1 – janeiro; 2 – fevereiro; ...; 12 – dezembro) e identificar o nome do mês e em que
trimestre o mês está incluído.

Informe o número do mês
1

O mês de janeiro é do primeiro trimestre do ano
'''
n = int(input('Informe o número do mês \n'))

mes = ''
trimestre = ''

if n == 1:
  print('O mês de janeiro é do primeiro trimestre do ano')
elif n == 2:
  print('O mês de feveiro é do primeiro trimestre do ano') 
elif n == 3:
  print('O mês de março é do primeiro trimestre do ano')
elif n == 4:
  print('O mês de abril é do segundo trimestre do ano')
elif n == 5:
  print('O mês de maio é do segundo trimestre do ano')
elif n == 6:
  print('O mês de junho é do segundo trimestre do ano')  
elif n == 7:
  print('O mês de julho é do terceiro trimestre do ano')
elif n == 8:
  print('O mês de agosto é do terceiro trimestre do ano')
elif n == 9:
  print('O mês de setembro é do terceiro trimestre do ano')    
elif n == 10:
  print('O mês de outubro é do quarto trimestre do ano')    
elif n == 11:
  print('O mês de novembro é do quarto trimestre do ano')     
elif n == 12:
  print('O mês de dezembro é do quarto trimestre do ano')      
