class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome
  
  def emitir_som(self):
    pass


class Mamifero(Animal):
  def amamentar(self):
    return f"O animal {self.nome} está amamentando"
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando."
  
class Morcego(Mamifero, Ave):
  def emitir_som(self):
     return "Morcegos emitem sons ultrassônicos"
  
morcego = Morcego(nome="Jeronima")

print("Nome: ", morcego.nome)
print("Som do morcego: ", morcego.emitir_som())

# Acessando métodos da classe mamíferos e classe ave
print("Classe Mamifero: ", morcego.amamentar())
print("Classe Ave: ", morcego.voar())