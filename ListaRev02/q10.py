'''
10. Ler uma frase e mostrar as strings obtidas a partir desta, passando uma a uma a letra inicial para o final, até
que a frase inicial seja apresentada.

Digite uma frase:
Brasil

rasilB
asilBr
silBra
ilBras
lBrasi
Brasil
'''

frase = input('Digite uma frase: \n')
for x in range(len(frase)):
  substring = frase.replace(frase[0], '')
  frase = substring + frase[0]
  print(frase)
