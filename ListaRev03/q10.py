'''
10. Retornar a palavra em uma determinada posição de um texto, contando a partir de zero, dados o texto e a posição da palavra,
utilizando a função Palavra (sem utilizar split), abaixo:

def Palavra(texto, pos)
'''

#Forma simples, usando split

#def Palavra(texto, pos):
#  texto = texto.split()
#  return texto[pos]

#Sem usar split, como a questão pede

def Palavra(texto, pos):
  palavras = []
  palavra = ''
  for x in texto:
    if x == ' ':
      palavras.append(palavra)
      palavra = ''
    else:
      palavra += x
  palavras.append(palavra)    
  return palavras[pos] 
  

texto = input()
pos = int(input())
print(Palavra(texto, pos))


  
