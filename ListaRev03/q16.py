'''
16. Verificar se um número é primo, utilizando a função Primo, abaixo:

def Primo(n)
'''

def Primo(n):
  count = 0
  for x in range(2, n):
    if n % x == 0:
      count+=1
  if count == 0:
    isPrimo = 'Sim, é primo'
  else:
    isPrimo = 'Não é primo'
  return isPrimo  

n = int(input())
print(Primo(n))
