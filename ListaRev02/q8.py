'''
8. Ler uma frase e mostrar a última letra de cada palavra.

Digite uma frase:
Técnico em Informática para Internet

omaat
'''
frase = list(input('Digite uma frase: \n').split())
for x in frase:
  print(x[len(x) - 1], end='')
