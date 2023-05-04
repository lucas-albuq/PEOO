'''
3. Mostrar a sequência de números abaixo.

Resultado: 1 -2 3 -4 5 -6 7 -8 9 -10
'''

for x in range(1, 11):
  if x % 2 == 0:
    x *= -1
  print(x, end=' ')
