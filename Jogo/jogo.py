# Personagem: Classe Mãe
# Herói: Classe derivado do Personagem 
# Inimigo : Classe derivado do Personagem 
import random

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
  
  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida < 0:
      self.__vida = 0 
  
  def atacar(self, alvo):
    dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} atacou {self.get_nome()} e causou {dano} de dano! ")
  

class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade) -> None:
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidades: {self.get_habilidade()}\n"
  
  def ataque_especial(self, alvo):
    dano = random.randint(self.get_nivel() * 4, self.get_nivel() * 8)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e casou {dano} de dano.")
  

class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo) -> None:
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo
  
  def get_tipo(self):
    return self.__tipo
  

# heroi = Heroi(nome="Batman", vida=100, nivel=5, habilidade="Super força")
# print(heroi.exibir_detalhes())

# inimigo = Inimigo(nome="Coringa", vida=100, nivel=3, tipo="Voador")
# print(inimigo.exibir_detalhes())
  
class Jogo:
  """Classe orquestradora do jogo"""
  def __init__(self) -> None:
    self.heroi = Heroi(nome="Batman", vida=65, nivel=5, habilidade="Super força")
    self.inimigo = Inimigo(nome="Coringa", vida=50, nivel=5, tipo="Voador")
  
  def iniciando_batalha(self):
    """Fazer a gestão da batalha em turnos"""
    print("Iniciando batalhas!")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes dos personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar...")
      escolha = input("Escolha (1 - Ataque normal, 2 - Ataque especial): ")

      if escolha == '1':
        self.heroi.atacar(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida. Escolha novamente!")

      if self.inimigo.get_vida() > 0:
        # Inimigo ataca o herói
        self.inimigo.atacar(self.heroi)
    if self.heroi.get_vida() > 0:
      print("\nParabéns, você venceu a batalha!")
    else:
      print("\nVocê foi derrotado!")



# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciando_batalha()

