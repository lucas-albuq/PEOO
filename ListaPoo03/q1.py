class Retangulo:
  def __init__(self, b, h):
    self.SetBase(b)
    self.SetAltura(h)
  def SetBase(self, b):
    if b > 0: self.__b = b
    else: raise ValueError()
  def SetAltura(self, h):
    if h > 0: self.__h = h
    else: raise ValueError()
  def GetBase(self):
    return self.__b
  def GetAltura(self):
    return self.__h
  def CalcArea(self):
    return self.__b*self.__h
  def CalcDiagonal(self):
    return (self.__b**2+self.__h**2)**0.5
  def __str__(self):
    return f"Base - {self.__b} \nAltura - {self.__h}"

class UI:
  @staticmethod
  def main():
    rect = Retangulo(float(input('Digite a base do retângulo: ')), float(input('Digite a altura do retângulo: ')))
    print(rect)
    print(f"Área do retângulo: {rect.CalcArea()}")
    print(f"Diagonal do retângulo: {rect.CalcDiagonal()}")
UI.main()
                  
