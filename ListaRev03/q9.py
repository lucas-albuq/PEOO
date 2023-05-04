'''
9. Obter todas as vogais em um texto, na sequência em que aparecem, utilizando a função Vogais abaixo:

def Vogais(texto)
'''
def Vogais(texto):
  vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
  vogaisTexto = ''
  for x in texto:
    if x in vogais:
      vogaisTexto += x
  return vogaisTexto    

texto = input()
print(f'Vogais = {Vogais(texto)}')
