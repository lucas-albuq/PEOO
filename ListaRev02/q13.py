'''
13. Ler uma frase e mostrar de trás para frente.

Digite uma frase:
Técnico em Informática para Internet

tenretnI arap acitámrofni me ocincéT
'''
#Jeito Fácil 

#frase = input('Digite uma frase: \n')
#print(frase[::-1])

#Jeito usando estruturas de repetição

frase = list(input('Digite uma frase: \n'))
for y in range(len(frase)):
  frase.insert(y, frase[len(frase)- 1])
  del(frase[len(frase) - 1])
resposta = ''.join(frase)   
print(resposta)
  
