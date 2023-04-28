'''
3. Ler quatro números inteiros, calcular a soma dos números pares e a soma dos números ímpares.
Digite quatro valores inteiros
1
2
3
4
Soma dos pares = 6
Soma dos ímpares = 4
'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

somaPares = 0
somaImpares = 0

lista = [n1, n2, n3, n4]

for x in lista:
  if x % 2 == 0:
    somaPares += x
  else:
    somaImpares += x
print(f'Soma dos pares = {somaPares}')
print(f'Soma dos ímpares = {somaImpares}')    
