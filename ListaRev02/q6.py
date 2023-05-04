'''
6. Mostrar a sequência de números abaixo.

Resultado: 1 2 3 6 4 5 6 15 7 8 9 24 ... 28 29 30 87

Obs: Sequência de valores de 1 a 30, incluindo a cada três valores a soma dos três elementos anteriores.
'''
count = 0
qtd = 0
for x in range(1, 31):
  if qtd == 3:
    print(count, end=' ')
    count = 0
    qtd = 0
  print(x, end=' ')
  count+=x
  qtd +=1 
print(count)
