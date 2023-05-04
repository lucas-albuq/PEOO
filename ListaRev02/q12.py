'''
12. Ler uma frase e contar o número de palavras.

Digite uma frase:
Técnico em Informática para Internet

5
'''
#Aqui está o jeito fácil de fazer, mas como o professor quer que use estruturas de repetição, vou fazer do jeito difícil.

#frase = list(input('Digite uma frase: \n').split())
#print(len(frase))

frase = list(input('Digite uma frase: \n').split())
count = 0

for x in frase:
  count+=1
print(count)  
