'''
8. Obter a soma dos números inteiros em um intervalo fechado [inicio, fim], utilizando a função Soma abaixo:

def Soma(inicio, fim)
'''
#Esse esquema de maior e menor é para funcionar mesmo com o início e o fim invertidos, ex: Soma(1, 10) = 55... Soma(10, 1) = 55
def Soma(inicio, fim):
  sum = 0
  maior = inicio
  menor = fim
  if fim > inicio:
    maior = fim
    menor = inicio
  for x in range(menor, maior + 1):
    sum+=x
  return sum  

inicio, fim = map(int, input().split())
print(f'Soma = {Soma(inicio, fim)}')
