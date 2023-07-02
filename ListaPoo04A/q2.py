import datetime
class Musica:
  def __init__(self, titulo, artista, album, datainclusao, duracao):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
    self.__dataInclusao = datainclusao
    self.__duracao = duracao
  def get_duracao(self):
    return self.__duracao
  def __str__(self):
    return f"Título - {self.__titulo}\nArtista - {self.__artista}\nÁlbum - {self.__album}\nData de inclusão - {self.__dataInclusao}\nDuração - {self.__duracao}"
class PlayList:
  def __init__(self, nome, descricao):
    self.__nome = nome
    self.__descricao = descricao
    self.__musicas = []
  def Inserir(self, m):
    self.__musicas.append(m)
  def Listar(self):
    return self.__musicas
  def TempoTotal(self):
    duracao = datetime.timedelta()
    for m in self.__musicas:
      duracao += m.get_duracao()
    return duracao
class UI:
  @staticmethod
  def main():
    playlist = PlayList("Playlist de Infoweb", "essa é uma playlist de infoweb")
    op = int(input("1 - Inserir música, 2 - Listar músicas, 3 - Tempo de duração, 4 - Fim\n"))
    while op!= 4:
      if op == 1:
        titulo = input("Insira o título:\n")
        artista = input("Insira o artista:\n")
        album = input("Insira o álbum:\n")
        dataInclusao = datetime.date.today()
        mm, ss = map(int, input("Insira a duração (mm:ss):\n").split(":"))
        duracao = datetime.timedelta(minutes = mm, seconds = ss)
        musica = Musica(titulo, artista, album, dataInclusao, duracao)
        playlist.Inserir(musica)
      elif op == 2:
        print(*playlist.Listar())
      elif op == 3:
        print(playlist.TempoTotal())
      op = int(input("1 - Inserir música, 2 - Listar músicas, 3 - Tempo de duração, 4 - Fim\n"))
UI.main()
