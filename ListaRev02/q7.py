'''
7. Ler uma frase e mostrar as strings obtidas a partir desta, removendo uma a uma a palavra no início.

Digite uma frase:
Técnico em Informática para Internet

Técnico em Informática para Internet
em Informática para Internet
Informática para Internet
para Internet
Internet
'''
frase = list(input('Digite uma frase: \n').split())
for x in range(len(frase)):
  resposta = ' '.join(frase)
  del(frase[0])
  print(resposta)
