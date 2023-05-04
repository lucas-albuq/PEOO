'''
17. Ler uma frase e mostrar cada palavra repetidas vezes de acordo com o número de vogais. (Desprezar os
acentos)

Digite uma frase:
Tecnico em Informatica para Internet

Tecnico Tecnico Tecnico em Informatica Informatica Informatica Informatica Informatica para para Internet
Internet Internet
'''

frase = input('Digite uma frase: \n').split()
vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
for palavra in frase:
  qtd = 0
  for caractere in palavra:
    if caractere in vogais:
      qtd+=1
  for x in range(qtd):
    print(palavra, end=' ')
  
