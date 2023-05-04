'''
18. Ler uma sequência de números inteiros separados por vírgula e calcula a soma destes valores.

Digite uma sequência de números separados por vírgula:
1,2,3,4,5

Soma = 15
'''
numeros = map(int, input().split(','))
sum = 0
for x in numeros:
  sum+=x
print(f'Soma = {sum}')  
