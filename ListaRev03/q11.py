'''
11. Gerar uma senha a partir de um texto formada pelo número de caracteres de cada palavra do texto, utilizando
a função Senha abaixo:

def Senha(texto)
'''
def Senha(texto):
  texto = texto.split()
  senha = ''
  for x in texto:
    senha+= str(len(x))
  return senha  

texto = input()
print(f'Senha = {Senha(texto)}')
