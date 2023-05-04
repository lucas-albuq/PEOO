'''
12. Remover espaços desnecessários entre palavras de um texto.

def RemoverEspacos(texto)
'''
def RemoverEspacos(texto):
  texto = texto.split()
  semEspacos = ' '.join(texto)
  return semEspacos

texto = input()
print(RemoverEspacos(texto))
