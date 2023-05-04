'''
14. Ler uma frase e mostrar cada uma de suas palavras separadamente e de trás para frente.

Digite uma frase:
Técnico em Informática para Internet

ocincéT
me
acitámrofni
arap
tenretnI
'''

frase = input('Digite uma frase: \n')
frase = list(frase[::-1].split())
for x in range(len(frase)):
  print(frase[len(frase) - 1 - x])

