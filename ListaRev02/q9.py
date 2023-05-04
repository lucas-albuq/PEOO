'''
9. Ler uma frase e mostrá-la repetidas vezes, de acordo com o número de caracteres desta, informando o número
da repetição antes da frase.

Digite uma frase:
Brasil

1 - Brasil
2 - Brasil
3 - Brasil
4 - Brasil
5 - Brasil
6 - Brasil
'''
frase = input('Digite uma frase: \n')
for x in range(1, len(frase) + 1):
  print(f'{x} - {frase}')
