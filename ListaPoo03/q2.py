class Frete:
  def __init__(self, d, p):
    self.SetDistancia(d)
    self.SetPeso(p)
  def SetDistancia(self, d):
    if d > 0: self.__d = d
    else: raise ValueError()
  def SetPeso(self, p):
    if p > 0: self.__p = p
    else: raise ValueError()
  def GetDistancia(self):
    return self.__d
  def GetPeso(self):
    return self.__p
  def CalcFrete(self):
    return (0.01 * self.__p)*self.__d #1 centavo de real para cada Kg transportado por Km
  def __str__(self):
    return f"Distância - {self.__d}Km \nPeso - {self.__p}Kg"
class UI:
  @staticmethod
  def main():
    frete = Frete(float(input('Digite a distância em Km: ')), float(input('Digite o peso em Kg: ')))
    print(frete)
    print(f'O frete será de R${frete.CalcFrete():.2f}')
UI.main()  
    
