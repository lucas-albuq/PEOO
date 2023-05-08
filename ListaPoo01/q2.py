'''
I. Implementar classes em Python para representar:

2. Uma Disciplina
A classe deve ter atributos para armazenar o nome da disciplina e as notas dos quatros bimestres e da prova final.
Os métodos da classe devem permitir calcular a média parcial (com as notas bimestrais) e a média final (com todas
as notas, caso o aluno tenha ficado em prova final). Considere como média de aprovação o valor 60, notas de 0 a
100, média parcial ponderada com pesos 2, 2, 3 e 3 e média final como a média aritmética da média parcial com a
nota da prova final, caso o aluno não seja aprovado por média.
Escrever um programa para testar a classe.
'''
class Disciplina:
  def __init__(self):
    self.nome = ''
    self.nota1 = 0
    self.nota2 = 0
    self.nota3 = 0
    self.nota4 = 0
    self.provaFinal = 0
  def calc_mediaParcial(self):    
    return ((self.nota1 * 2) + (self.nota2 * 2) + (self.nota3 * 3) + (self.nota4 * 3))/10
  def calc_mediaFinal(self):
    return (self.calc_mediaParcial() + self.provaFinal)/2

x = Disciplina()

print('Digite o nome da disciplina:')
x.nome = input()
print('Digite a nota do primeiro bimestre:')
x.nota1 = int(input())
print('Digite a nota do segundo bimestre:')
x.nota2 = int(input())
print('Digite a nota do terceiro bimestre:')
x.nota3 = int(input())
print('Digite a nota do quarto bimestre:')
x.nota4 = int(input())

print("Media parcial = ", x.calc_mediaParcial())

if x.calc_mediaParcial() < 60:
  print('Digite a nota da prova final:')
  x.provaFinal = int(input())
  print('Média Final = ', x.calc_mediaFinal())
