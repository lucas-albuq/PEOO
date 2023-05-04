'''
14. Ler três valores e dizer se eles formam um triângulo. Caso afirmativo, dizer seu tipo (equilátero, isósceles ou
escaleno).

Digite três valores:
1
2
10

Esses valores não formam um triângulo
'''

print('Digite três valores:')
a = int(input())
b = int(input())
c = int(input())

formaTriangulo = False
if abs(b - c) < a < b + c:
  formaTriangulo = True
elif abs(a - c) < b < a + c:
  formaTriangulo = True
elif abs(a - b) < c < a + b:
  formaTriangulo = True

if formaTriangulo == True:
  if a == b == c:
    print('Esses valores formam um triângulo equilátero')
  elif a == b or a == c or b == c:
    print('Esses valores formam um triângulo isósceles')
  else:
    print('Esses valores formam um triângulo escaleno')
else:
  print('Esses valores não formam um triângulo')
