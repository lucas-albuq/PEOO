'''
5. Mostrar a sequência de números abaixo.

Resultado: 1 2 4 7 11 16 22 29 37 46

Obs: Sequência inicia com 1, a partir daí, soma o primeiro valor com 1, o segundo valor com 2, o terceiro com 3, o
quarto por 4 e assim por diante.
'''
x = 1
for y in range(1, 11):
  print(x, end=' ')
  x+=y
