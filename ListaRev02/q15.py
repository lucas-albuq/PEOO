'''
15. Ler uma frase e montar uma senha formada pelo número de caracteres de cada palavra.

Digite uma frase:
Técnico em Informática para Internet

721148
'''

frase = input('Digite uma frase: \n').split()
senha = ''
for palavra in frase:
  senha += str(len(palavra))
print(senha)  
 
