primeiraNota = input()
segundaNota = input()

notaDecimalUm = float(primeiraNota)
notaDecimalDois = float(segundaNota)

pesoUm = float(3.5)
pesoDois = float(7.5)

mediaAritmedica = ((notaDecimalUm * pesoUm) + (notaDecimalDois * pesoDois)) / (pesoUm + pesoDois)
    
print(f'MEDIA = {mediaAritmedica:,.5f}')
