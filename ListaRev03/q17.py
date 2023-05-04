'''
17. Calcular a velocidade média em Km/h de um atleta numa prova de corrida dada a distância percorrida em
quilômetros e o tempo gasto no formato “hh:mm:ss” utilizando a função VelocidadeMedia abaixo:

def VelocidadeMedia(distancia, tempo)
'''
def VelocidadeMedia(distancia, tempo):
  h, m, s = map(int, tempo.split(':'))
  m = (m*60 + s)/60
  h = (h*60 + m)/60
  vel = str(distancia / h) + ' Km/h'
  return vel

distancia = int(input())
tempo = input()

print(VelocidadeMedia(distancia, tempo))  
  
