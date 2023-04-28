'''
7. Calcular as raízes reais da equação aX2 + bX + c = 0, dados a, b e c. Se a equação não tiver raízes reais, mostrar a mensagem: “impossível calcular”.

Digite os coeficientes a, b, e c de uma equação do II grau
1
0
-4

As raízes são 2 e -2
'''

a = int(input('Digite os coeficientes a, b e c de uma equação do II grau \n'))
b = int(input())
c = int(input())

delta = b**2 - 4 * a * c

if delta < 0:
  print('impossível calcular')
else:  
  raiz1 = ((b * -1) + (delta)**0.5) / 2 * a
  raiz2 = ((b * -1) - (delta)**0.5) / 2 * a

  if raiz1 == raiz2:
    print(f'A raiz é {raiz1}')
  else:  
    print(f'As raízes são {raiz1} e {raiz2}')
