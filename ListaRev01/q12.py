'''
12. Ler uma string com dois valores inteiros positivos entre um operador ( +, –, * ou / ) e calcular o resultado da
operação matemática utilizando estes valores e o operador.

Digite dois valores inteiros separados por um operador +, -, * ou /
20+100

O resultado da operação é 120
'''
operacao = input('Digite dois valores inteiros separados por um operador +, -, * ou / \n')
if '+' in operacao:
  a, b = map(int, operacao.split('+'))
  calc = a + b
elif '-' in operacao:
  a, b = map(int, operacao.split('-')) 
  calc = a - b
elif '*' in operacao:
  a, b = map(int, operacao.split('*'))
  calc = a * b
elif '/' in operacao:
  a, b = map(int, operacao.split('/'))
  calc = a / b
print(f'O resutado da operação é {calc}')  
