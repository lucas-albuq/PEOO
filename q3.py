'''QUESTÃO 03
Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3).
Considerar as notas com valores inteiros entre zero e cem.

Digite a nota do primeiro bimestre da disciplina:
50
Digite a nota do segundo bimestre da disciplina:
70

Média parcial = 62
'''

notaPrimeiroBimestre = int(input('Digite a nota do primeiro bimestre da disciplina:\n'))
notaSegundoBimestre = int(input('Digite a nota do segundo bimestre da disciplina:\n'))

peso1 = 2
peso2 = 3

mediaParcial = ((notaPrimeiroBimestre * peso1) + (notaSegundoBimestre * peso2)) / (peso1 + peso2)

if int(mediaParcial) == mediaParcial:
    mediaParcial = int(mediaParcial)
    
print(f'Média parcial = {mediaParcial}')
