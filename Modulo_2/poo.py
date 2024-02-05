# Paradigma de organização em torno de objetos 

# Classe

class Pessoa:
  # construtor
  def __init__(self, nome, idade) -> None:
    self.nome = nome
    self.idade = idade

  def saudacao(self):
    return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Objeto criado a partir da Classe
pessoa1 = Pessoa("Grazielli", 27)
print("Nome: ", pessoa1.nome)
print("Nome: ", pessoa1.idade)
print("Saudação: ", pessoa1.saudacao())

pessoa2 = Pessoa("Beyoncé", 42)
mensagem = pessoa2.saudacao()
print(mensagem)

# Vantagens: 
  # Reutulização de código
  # Organização e estrutura
  # Os três pilares do POO: Encapsulamento, Poliformismo e Herança.

# Desvantagens 
  # Complexidade
  