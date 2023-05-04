'''
19. Mostrar a tabuada de 1 a 10.

Tabuada de 1
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10

Tabuada de 2
2 x 1 = 2
2 x 2 = 4
...
2 x 10 = 20
...
Tabuada de 10
10 x 1 = 10
10 x 2 = 20
...
10 x 10 = 100
'''

for x in range(1, 11):
  print(f'Tabuada de {x}')
  for y in range(1, 11):
    print(f'{x} x {y} = {x*y})
  print('') #Botei esse print vazio só pra quebrar linha ao final de cada tabuada        
