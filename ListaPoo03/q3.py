class Equacao:
  def __init__(self, a, b, c):
    self.SetA(a)
    self.SetB(b)
    self.SetC(c)
  def SetA(self, a):
    if a != 0: self.__a = a # a diferente de 0 para existir uma equação do 2 grau
    else: raise ValueError()
  def SetB(self, b):
    self.__b = b #única condição é que seja um valor real
  def SetC(self, c):
    self.__c = c #única condição é que seja um valor real
  def GetA(self):
    return self.__a
  def GetB(self):
    return self.__b
  def GetC(self):
    return self.__c
  def Delta(self):
    return self.__b**2 - 4 * self.__a * self.__c #b² - 4ac
  def TemRaizesReais(self):
    if self.Delta() < 0: return False
    else: return True
  def Raiz1(self):
    return (-self.__b + self.Delta()**0.5)/(2*self.__a)
  def Raiz2(self):
    return (-self.__b - self.Delta()**0.5)/(2*self.__a)
  def __str__(self):
    return f"a - {self.__a}, b - {self.__b}, c - {self.__c}"
class UI:
  @staticmethod
  def main():
    eq = Equacao(float(input("Digite o valor de a: ")), float(input("Digite o valor de b: ")), float(input("Digite o valor de c: ")))
    print(eq)
    print(f'Delta = {eq.Delta()}')
    print(f'Tem raízes reais: {eq.TemRaizesReais()}')
    print(f'Raizes = {eq.Raiz1()}, {eq.Raiz2()}')
UI.main()    
