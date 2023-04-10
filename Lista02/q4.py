''' QUESTÃO 04
Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores
podem ser números reais. Mostrar o resultado com duas casas decimais.

Digite a base e a altura do retângulo
3
4

Área = 12.00 - Perímetro = 14.00 - Diagonal = 5.00
'''

baseRect = int(input('Digite a base e a altura do retângulo\n'))
alturaRect = int(input())

areaRect = baseRect * alturaRect
perimetroRect = baseRect * 2 + alturaRect * 2
diagonalRect = (baseRect**2 + alturaRect**2) ** (1/2)

print(f'Área = {areaRect:.2f} - Perímetro = {perimetroRect:.2f} - Diagonal = {diagonalRect:.2f}')