'''
13. Formatar um nome próprio deixando no formato para referências bibliográficas: último sobrenome, seguido
das iniciais dos demais nomes, utilizando a função Referencia, abaixo:

def Referencia(nome)
'''

def Referencia(nome):
  nome = list(nome.split())
  referencia = nome[len(nome) - 1]+','
  del(nome[len(nome) - 1])
  string = ''
  for x in nome:
    if x != 'de':
      string+=' ' + x[0] + '.'
  referencia += string
  return referencia

nome = input()
print(Referencia(nome))
    
