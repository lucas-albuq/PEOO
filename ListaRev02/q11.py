'''
11. Ler uma string, calcular e mostrar a soma dos caracteres que são algarismos.

Digite uma frase:
Brasil 2014

7
'''
frase = input('Digite uma frase: \n')
sum = 0
for x in frase:
  try:
    int(x)
    isInteger = True
  except ValueError:
    isInteger = False
  if isInteger == True:
    sum+= int(x)
print(sum)    
