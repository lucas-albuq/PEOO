'''
4. Mostrar a sequência de números abaixo.

Resultado: 1 2 -3 4 5 -6 7 8 -9 10 11 -12 ... 28 29 -30

Obs: Sequência de 1 a 30, mas com os múltiplos de 3 com sinal negativo.
'''

for x in range(1, 31):
  if x % 3 == 0:
    x *= -1
  print(x, end=' ')
