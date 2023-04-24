'''
2. Ler quatro valores inteiros, calcular e mostrar a média aritmética entre eles. Mostrar também os números
menores e os números maiores ou iguais à média.

Digite quatro valores inteiros
1
2
3
10

Média = 4
Números menores que a média
1
2
3
Números maiores ou iguais à média
10
'''
print('Digite quatro valores inteiros')
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
numbers = [n1, n2, n3, n4]

media = sum(numbers) / len(numbers)
print(f'Média = {media}')

menores = []
maiores = []

for x in numbers:
  if x < media:
    menores.append(x)
  else:
    maiores.append(x)

print('Números menores que a média')

for i in menores:
  print(i)

print('Números maiores ou iguais a média')
for y in maiores:
  print(y)
