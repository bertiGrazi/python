# Personagem: Classe Mãe
# Herói: Classe derivado do Personagem 
# Inimigo : Classe derivado do Personagem 

class Personagem:
  def __init__(self, nome, vida, nivel) -> None:
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel 

  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida
  
  def get_nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade) -> None:
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidades: {self.get_habilidade()}\n"
  

class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo) -> None:
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo
  
  def get_tipo(self):
    return self.__tipo
  


heroi = Heroi(nome="Batman", vida=100, nivel=5, habilidade="Super força")
print(heroi.exibir_detalhes())

inimigo = Inimigo(nome="Coringa", vida=100, nivel=3, tipo="Voador")
print(inimigo.exibir_detalhes())