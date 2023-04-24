'''3. Retornar as iniciais do nome de uma pessoa dado seu nome completo, usando a função Iniciais abaixo. O
programa deve solicitar do usuário seu nome completo e mostrar as iniciais obtidas pela função.

def iniciais(nome)
'''

def iniciais(nome):
  palavras = nome.split()
  resultado = ''
  for palavra in palavras:
    resultado += palavra[0]
  return resultado

nome = input('Escreva seu nome completo: ')
print(f'As iniciais do seu nome são: {iniciais(nome)}')
  
